
from django.http import HttpResponse,HttpResponseRedirect
from models.models import User
from django.urls import reverse
from django.http import JsonResponse
from models.models import Topic
from models.models import Comments
from models.models import Events
from models.models import Revelation
from models.models import Revelation_Pic
from models.models import activity
from models.models import activity_contribute
from models.models import contributes_Pic
from Tools import func as tools

def post_topic(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == '-1':
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid=request.POST.get('uid')
    usr = User.objects.get(UID__exact=uid)

    if request.method=="POST":
        category=int(request.POST.get('category'))
        title=request.POST.get('title')
        statement=request.POST.get('statement')
        tag=request.POST.get('tag')

        #用户等级权限判断
        if tools.check_right(usr.rank)!='full':
            result['res']='permission denied'
            return JsonResponse(result)

        #用户经验值更新
        usr.EXP+=15
        #用户等级更新
        usr.rank=tools.exp2rank(usr.EXP)
        usr.save()
        tmpTime=tools.getTime()

        try:
            Topic.objects.create(UID=usr.UID,category=category,title=title,statement=statement,Tag=tag,
                             time=tmpTime,star=0,tip_off=0,status=False,isPostByEditor=False,
                             Fcounts=0,lastUpDateTime=tmpTime)

        except Exception as e:
            print(e)
            result['res'] = 'failed'
            return JsonResponse(result)
        
        result['res']='ok'
        return JsonResponse(result)

def post_comment(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == '-1':
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid=request.POST.get('uid')


    if request.method=='POST':

        try:
           TID = int(request.POST.get('TID'))
           value = request.POST.get('value')
           Comments.objects.create(UID=uid,TID=TID,value=value,time=tools.getTime(),star=0,status=False,tip_off=0)
           # 用户经验值更新
           tools.addEXP(1,4)
        except Exception as e:
           print(e)
           result['res']='failed'
           return JsonResponse(result)

        result['res']='ok'
        return JsonResponse(result)

def post_event(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == '-1':
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid=request.POST.get('uid')

    #权限检查
    usr=User.objects.get(UID__exact=uid)
    if usr.ifPassedExam==False:
        result['res']='permission denied'
        return JsonResponse(result)

    if request.method=='POST':
        tid=int(request.POST.get('TID'))
        title=request.POST.get('title')
        statement=request.POST.get('statement')
        url=request.POST.get('url')
        eventTime=request.POST.get('eventTime')

        try:
            #更新话题最后更新时间
            tmpTime=tools.getTime()
            topic=Topic.objects.get(TID__exact=tid)
            topic.lastUpDateTime=tmpTime
            topic.save()

            Events.objects.create(TID=tid,UID=uid,time=tmpTime,title=title,statement=statement
                                  ,star=0,tip_off=0,status=False,isPostByEditor=False,url=url,eventTime=eventTime)

            #exp
            tools.addEXP(uid,10)

        except Exception as e :
            print(e)
            result['res']='failed'
            return JsonResponse(result)

        result['res'] = 'ok'
        return JsonResponse(result)

def post_revelation(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == '-1':
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid = request.POST.get('uid')

    # 权限检查
    usr = User.objects.get(UID__exact=uid)
    if usr.ifPassedExam == False:
        result['res'] = 'permission denied'
        return JsonResponse(result)

    if request.method == 'POST':
        tid = int(request.POST.get('TID'))
        title = request.POST.get('title')
        statement = request.POST.get('statement')
        eventTime = request.POST.get('eventTime')
        text=request.POST.get('text')


        try:
            # 更新话题最后更新时间
            tmpTime = tools.getTime()
            topic = Topic.objects.get(TID__exact=tid)
            topic.lastUpDateTime = tmpTime
            topic.save()

            R=Revelation.objects.create(TID=tid, UID=uid, time=tmpTime, title=title, statement=statement
                                  , star=0, tip_off=0, status=False, isPostByEditor=False, eventTime=eventTime,text=text)

            picsUPload = request.FILES.getlist('imgs')
            try:
                for f in picsUPload:
                    Revelation_Pic.objects.create(RID=R.RID,img=f)
            except Exception as e1:
                print(e1)
                result['res'] = 'failed'
                return JsonResponse(result)
            # exp
            tools.addEXP(uid, 10)

        except Exception as e:
            print(e)
            result['res'] = 'failed'
            return JsonResponse(result)

        result['res'] = 'ok'
        return JsonResponse(result)

def post_Activity(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == '-1':
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid = request.POST.get('uid')

    # 权限检查
    usr = User.objects.get(UID__exact=uid)
    if usr.isEDIT == False:
        result['res'] = 'permission denied'
        return JsonResponse(result)

    if request.method=='POST':
        title=request.POST.get('title')
        introduction=request.POST.get('introduction')
        reward=int(request.POST.get('reward'))
        poster = request.FILES.get('poster')

        try:
            activity.objects.create(reward=reward,poster=poster,Introduction=introduction,Title=title,isEND=False)
        except Exception as e:
            print(e)
            result['res']='failed'
            return JsonResponse(result)

        result['res']='ok'
        return JsonResponse(result)


def post_activity_contribute(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == '-1':
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid = int(request.POST.get('uid'))


    if request.method == 'POST':
        aid = int(request.POST.get('AID'))
        title = request.POST.get('title')
        statement = request.POST.get('statement')
        text = request.POST.get('text')
        try:
            ac = activity_contribute.objects.create(AID=aid, UID=uid, time=tools.getTime(), title=title, statement=statement
                                          , star=0, tip_off=0, status=False, text=text)

            picsUPload = request.FILES.getlist('imgs')
            try:
                for f in picsUPload:
                    contributes_Pic.objects.create(A_CID=ac.A_CID,img=f)
            except Exception as e1:
                print(e1)
                result['res'] = 'failed'
                return JsonResponse(result)
            # exp
            a=activity.objects.get(AID__exact=aid)
            tools.addEXP(uid, a.reward)


        except Exception as e:
            print(e)
            result['res'] = 'failed'
            return JsonResponse(result)

        result['res'] = 'ok'
        return JsonResponse(result)