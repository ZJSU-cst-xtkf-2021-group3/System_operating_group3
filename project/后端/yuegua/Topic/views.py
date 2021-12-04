from django.http import HttpResponse,HttpResponseRedirect
from models.models import User
from django.urls import reverse
from django.http import JsonResponse
from models.models import Topic,userFollow_topic,topic_vote
from Tools import func as tools
from models.models import Tip_off,Star


def Topic_tip_off(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)

    tid=int(request.GET.get('TID'))
    try:
        t=Topic.objects.get(TID__exact=tid)
        Tip_off.objects.create(type=1,valueID=tid,UID=t.UID,points=50)
        t.tip_off+=1
        t.save()

    except Exception as e:
        print(e)
        result['res'] = 'failed'
        return JsonResponse(result)

    result['res']="ok"
    return JsonResponse(result)


def Topic_star(request):
    result = {
        'res': ''
    }
    uid = request.session.get('uid', -1)
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid=int(request.POST.get('uid'))
    tid=int(request.GET.get('TID'))
    try:
        t=Topic.objects.get(TID__exact=tid)
        tu=User.objects.get(UID__exact=t.UID)
        u=User.objects.get(UID__exact=uid)

        exist=Star.objects.filter(UID__exact=uid,type__exact=1,valueID__exact=tid)
        if exist or t.UID==uid:
            result['res']='refused'
            return JsonResponse(result)

        #add exp
        tools.addEXP(uid,3)
        tools.addEXP(tu.UID,5)

        #通知

        #推荐
        t.AgeRange_avg=int(((u.AgeRange+t.AgeRange_avg*(t.Fcounts+t.star))/(t.Fcounts+t.star+1))+0.5)
        t.save()
        # counts
        t.star += 1
        t.hotPoints =t.hotPoints+0.1
        t.save()

        #保存记录
        Star.objects.create(UID=uid,type=1,valueID=tid)
    except Exception as e:
        print(e)
        result['res']='failed'
        return JsonResponse(result)

    result['res']='ok'
    return JsonResponse(result)

def Subscribe(request):
    result = {
        'res': ''
    }
    uid = request.session.get('uid', -1)
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    uid=int(request.POST.get('uid'))
    tid = int(request.POST.get('TID'))

    try:
        t=Topic.objects.get(TID__exact=tid)
        tu=User.objects.get(UID__exact=t.UID)
        u=User.objects.get(UID__exact=uid)
        exist = userFollow_topic.objects.filter(UID__exact=uid, FTID__exact=tid)
        if exist or t.UID==uid:
            result['res'] = 'refused'
            return JsonResponse(result)
    except Exception as e:
        print(e)
        result['res']='failed'
        return JsonResponse(result)


    try:
        # exp:
        tools.addEXP(uid,3)
        tools.addEXP(tu.UID,8)

        #通知：

        # 推荐
        t.AgeRange_avg = int(((u.AgeRange + t.AgeRange_avg * (t.Fcounts + t.star)) / (t.Fcounts + t.star + 1)) + 0.5)
        t.save()
        # counts
        t.Fcounts += 1
        t.hotPoints =t.hotPoints+0.2
        t.save()
        #hot


        # 保存记录
        userFollow_topic.objects.create(FTID=tid,UID=uid,lastVisitTime=tools.getTime())
    except Exception as e:
        print(e)
        result['res'] = 'failed'
        return JsonResponse(result)

    result['res']='ok'
    return JsonResponse(result)

def show_topic_vote(request):
    result = {
        'res': ''
    }
    tid=int(request.GET.get('TID'))
    try:
        data=[]
        votesList=topic_vote.objects.filter(TID__exact=tid)
        for i in votesList:
            tmp={}
            tmp['ID']=i.ID
            tmp['item']=i.item
            tmp['counts']=i.counts
            data.append(tmp)
        result['data']=data
    except Exception as e :
        print(e)
        result['res']='failed'
        return JsonResponse(result)

    result['res']='ok'
    return JsonResponse(result)

def votes(request):
    result = {
        'res': ''
    }
    uid = request.session.get('uid', -1)
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    itemID=request.GET.get('ID')
    try:
        t=topic_vote.objects.get(ID__exact=itemID)
        t.counts+=1
        t.save()
    except Exception as e:
        result['res']='failed'
        print(e)
        return JsonResponse(result)
    result['res']='ok'
    return JsonResponse(result)

def show_topic_info(request):
    result = {
        'res': ''
    }
    try:
        data={}
        tid=int(request.GET.get('TID'))
        t=Topic.objects.get(TID__exact=tid)
        if t.status==False:
            result['res'] = 'refused'
            return JsonResponse(result)
        u=User.objects.get(UID__exact=t.UID)
        data['TID']=t.TID
        data['Author']=u.Uname
        data['Category']=t.category
        data['title']=t.title
        data['statement']=t.statement
        data['postTime']=tools.stamp2strtime(t.time)
        data['star']=t.star
        data['tip-off']=t.tip_off
        data['isPostByEditor']=t.isPostByEditor
        data['lastUpDateTime']=tools.stamp2strtime(t.lastUpDateTime)
        data['Fcounts']=t.Fcounts
        data['Tag']=t.Tag
        data['hotPoints']=t.hotPoints
        result['data']=data

    except Exception as e:
        result['res'] = 'failed'
        print(e)
        return JsonResponse(result)

    result['res'] = 'ok'
    return JsonResponse(result)