from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from models.models import User, activity,activity_contribute,activity_vote,Tip_off,Star,contributes_Pic
from django.urls import reverse
from django.http import JsonResponse
from Tools import func as tools

def info(request):
    result={}
    aid=request.GET.get("AID")
    try:
        a=activity.objects.get(AID__exact=aid)
        data={}
        data['AID']=a.AID
        data['title']=a.Title
        data['introduce']=a.Introduction
        data['isEND']=a.isEND
        data['reword']=a.reward
        data['poster']=a.poster.url
        result['data']=data
    except Exception as e:
        print(e)
        result['res']='failed'
        return JsonResponse(result)
    result['res']='ok'
    return JsonResponse(result)

def show_Activity_vote(request):
    result = {
        'res': ''
    }
    aid=request.GET.get("AID")
    try:
        data = []
        votesList = activity_vote.objects.filter(AID__exact=aid)
        for i in votesList:
            tmp = {}
            tmp['ID'] = i.ID
            tmp['item'] = i.item
            tmp['counts'] = i.counts
            data.append(tmp)
        result['data'] = data
    except Exception as e:
        print(e)
        result['res'] = 'failed'
        return JsonResponse(result)
    result['res'] = 'ok'
    return JsonResponse(result)

def vote(request):
    result = {
        'res': ''
    }
    uid = request.session.get('uid', -1)
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)

    itemID = request.GET.get('ID')
    try:
        t=activity_vote.objects.get(ID__exact=itemID)
        t.counts+=1
        t.save()
    except Exception as e:
        result['res']='failed'
        print(e)
        return JsonResponse(result)
    result['res']='ok'
    return JsonResponse(result)


def star(request):
    result = {
            'res': ''
        }

    uid = request.session.get('uid', -1)
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid=int(request.GET.get('uid'))
    acid=int(request.GET.get('A_CID'))
    try:
        ac=activity_contribute.objects.get(A_CID__exact=acid)
        acu=User.objects.get(UID__exact=ac.UID)
        exist=Star.objects.filter(UID__exact=uid,type__exact=5,valueID__exact=ac.A_CID)
        if exist or ac.UID==uid:
            result['res']='refused'
            return JsonResponse(result)

        #add exp
        tools.addEXP(uid,3)
        tools.addEXP(acu.UID,5)

        #通知

        # counts
        ac.star += 1
        ac.hotPoints+=0.1
        ac.save()

        #保存记录
        Star.objects.create(UID=uid,type=5,valueID=ac.A_CID)
    except Exception as e:
        print(e)
        result['res']='failed'
        return JsonResponse(result)

    result['res']='ok'
    return JsonResponse(result)

def tip_off(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)

    acid = int(request.GET.get('A_CID'))
    try:
        ac = activity_contribute.objects.get(A_CID__exact=acid)
        Tip_off.objects.create(type=5, valueID=ac.A_CID, UID=ac.UID, points=50)
        ac.tip_off += 1
        ac.save()

    except Exception as e:
        print(e)
        result['res'] = 'failed'
        return JsonResponse(result)

    result['res'] = "ok"
    return JsonResponse(result)

def all(request):
    result = {}
    List = []

    aid = request.GET.get('AID')
    try:
        contributesList = activity_contribute.objects.filter(Q(AID__exact=aid),Q(status__exact=True)).order_by('-hotPoints')
        for i in contributesList:
            data = {}
            data['A_CID'] = i.A_CID
            data['UID'] = i.UID
            data['Uname'] = User.objects.get(UID__exact=i.UID).Uname
            data['title'] = i.title
            data['time'] = tools.stamp2strtime(i.time)
            data['star'] = i.star
            data['tip_off'] = i.tip_off
            data['statement']=i.statement
            List.append(data)
    except Exception as e:
        print(e)
        result['res'] = 'failed'
        return JsonResponse(result)
    result['data'] = List
    result['res'] = 'ok'
    return JsonResponse(result)

def show_contributes(request):
    acid = int(request.GET.get("A_CID"))
    result = {
        'res': ''
    }
    try:
        ac = activity_contribute.objects.get(A_CID__exact=acid)
        if ac.status:
            pics = contributes_Pic.objects.filter(A_CID__exact=acid)
            picsList = [i.img.url for i in pics]
            tmp = {}
            tmp['pics'] = picsList
            tmp['text'] = ac.text
            tmp['ID'] = ac.A_CID
            tmp['Uname'] = User.objects.get(UID__exact=ac.UID).Uname
            tmp['time'] = tools.stamp2strtime(ac.time)
            tmp['title'] = ac.title
            tmp['statement'] = ac.statement
            tmp['star'] = ac.star
            tmp['tip-off'] = ac.tip_off
            result['data'] = tmp
    except Exception as e:
        print(e)
        result['res'] = 'failed'
        return JsonResponse(result)

    result['res'] = 'ok'
    return JsonResponse(result)


