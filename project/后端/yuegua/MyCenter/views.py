import json

from django.db.models import Q
from django.http import HttpResponse,HttpResponseRedirect
from models.models import User,userFollow_user,userPrivacy,userFollow_topic,Topic,Revelation,Events,Comments,Revelation_Pic
from django.urls import reverse
from django.http import JsonResponse
from Tools import func as tools


def basicInfo(request):
    result={
        'res':''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid=int(request.GET.get('uid',1))
    try:
        u=User.objects.get(UID__exact=uid)
        data={}
        data['EXP']=u.EXP
        data['rank']=u.rank
        data['ifPassedExam']=u.ifPassedExam
        data['Fcounts']=u.Fcounts
        data['isEditor']=u.isEDIT
        data['header']=tools.host+u.header.url
        data['introduction']=u.introduction
        data['Uname']=u.Uname
        data['percent']=tools.rankPercent(u.EXP,u.rank)

    except Exception as e:
        print(e)
        result['res']='failed'
        return JsonResponse(result)

    result['res']='ok'
    result['data']=data
    return JsonResponse(result)


def profile(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid=int(request.POST.get('uid',1))
    try:
        up=userPrivacy.objects.get(UID__exact=uid)
        if request.method=='GET':
            data = {}
            data['public_Ftopic'] = up.public_Ftopic
            data['public_Fuser'] = up.public_Fuser
            data['public_comments'] = up.public_comments
            data['public_events'] = up.public_events
            data['public_topics'] = up.public_topics
            result['res'] = 'ok'
            result['data'] = data
            return JsonResponse(result)

        if request.method=="POST":
            public_Ftopic= int(request.POST.get('public_Ftopic'))
            public_Fuser = int(request.POST.get('public_Fuser'))
            public_comments = int(request.POST.get('public_comments'))
            public_events = int(request.POST.get('public_events'))
            public_topics = int(request.POST.get('public_topics'))

            up.public_Ftopic=public_Ftopic
            up.public_Fuser=public_Fuser
            up.public_comments=public_comments
            up.public_events=public_events
            up.public_topics=public_topics
            up.save()

            result['res'] = 'ok'
            return JsonResponse(result)

    except Exception as e:
        print(e)
        result['res']='failed'
        return JsonResponse(result)


def del_subscribe(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    tid=int(request.GET.get("TID"))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid=int(request.GET.get('uid',1))

    try:
        slist=userFollow_topic.objects.get(Q(FTID__exact=tid),Q(UID__exact=uid))
        slist.delete()
        t=Topic.objects.get(TID__exact=tid)
        t.Fcounts-=1
        t.hotPoints=round(t.hotPoints-0.2,1)
        t.save()

    except Exception as e:
        print(e)
        result['res']='failed'
        return JsonResponse(result)

    result['res'] = 'ok'
    return JsonResponse(result)


def del_follow(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    tuid = int(request.GET.get("UID"))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid=int(request.GET.get('uid'))

    try:
        flist = userFollow_user.objects.get(Q(FUID__exact=tuid),Q(UID__exact=uid))
        flist.delete()
        t = User.objects.get(UID__exact=tuid)
        t.Fcounts-=1
        t.save()

    except Exception as e:
        print(e)
        result['res'] = 'failed'
        return JsonResponse(result)

    result['res'] = 'ok'
    return JsonResponse(result)


def my_subscribe(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid=int(request.GET.get('uid',1))

    try:
        slist=userFollow_topic.objects.filter(UID__exact=uid)
        data = []
        for i in slist:
            tmp_t = Topic.objects.get(TID__exact=i.FTID)
            u=User.objects.get(UID__exact=tmp_t.UID)
            if tmp_t.status:
                tmp = {}
                tmp['TID'] = i.FTID
                tmp['title'] = tmp_t.title
                tmp['statement'] = tmp_t.statement
                tmp['star'] = tmp_t.star
                tmp['tip_off'] = tmp_t.tip_off
                tmp['Fcounts']=tmp_t.Fcounts
                tmp['hotPoints'] = tmp_t.hotPoints
                tmp['mainPic'] = tools.host+tmp_t.mainPic.url
                tmp['lastUpDateTime'] = tmp_t.lastUpDateTime
                tmp['header']=tools.host+u.header.url
                tmp['Uname']=u.Uname
                tmp['Tag']=tmp_t.Tag
                data.append(tmp)
        data.sort(key=lambda x:x['lastUpDateTime'],reverse=True)
    except Exception as e:
        print(e)
        result['res']='failed'
        return JsonResponse(result)

    result['res'] = 'ok'
    result['data']=data
    return JsonResponse(result)

def my_follow(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid=int(request.GET.get('uid',1))
    try:
        list = userFollow_user.objects.filter(UID__exact=uid)
        data = []
        for i in list:
            tmp_u = User.objects.get(UID__exact=i.FUID)
            tmp = {}
            tmp['UID'] = i.FUID
            tmp['Uname'] = i.FUname
            tmp['header'] = tools.host+tmp_u.header.url
            tmp['introduction']=tmp_u.introduction
            data.append(tmp)
    except Exception as e:
        print(e)
        result['res'] = 'failed'
        return JsonResponse(result)

    result['res'] = 'ok'
    result['data'] = data
    return JsonResponse(result)


def my_topics(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid=int(request.GET.get('uid',1))
    try:
        u=User.objects.get(UID__exact=uid)
        list = Topic.objects.filter(UID__exact=uid)
        data = []
        for i in list:
            if i.status:
                tmp = {}
                tmp['header']=tools.host+u.header.url
                tmp['Uname']=u.Uname
                tmp['TID'] = i.TID
                tmp['status'] = i.status
                tmp['title'] = i.title
                tmp['statement'] = i.statement
                tmp['hotPoints'] = i.hotPoints
                tmp['lastUpDateTime'] =i.lastUpDateTime
                tmp['mainPic'] = tools.host+i.mainPic.url
                tmp['star']=i.star
                tmp['Fcounts']=i.Fcounts
                tmp['tip_off']=i.tip_off
                tmp['time']=tools.stamp2strtime(i.time)
                data.append(tmp)
    except Exception as e:
        print(e)
        result['res'] = 'failed'
        return JsonResponse(result)

    result['res'] = 'ok'
    result['data'] = data
    return JsonResponse(result)

def my_comments(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid = int(request.GET.get('uid', 1))
    try:
        list = Comments.objects.filter(UID__exact=uid)
        data = []
        for i in list:
            if i.status:
                tmp = {}
                tmp['Ttitle'] = Topic.objects.get(TID__exact=i.TID).title
                tmp['CID'] = i.CID
                tmp['status'] = i.status
                tmp['value'] = i.value
                tmp['hotPoints'] = i.hotPoints
                tmp['time'] = tools.stamp2strtime(i.time)
                tmp['star'] = i.star
                tmp['tip-off'] = i.tip_off
                data.append(tmp)
    except Exception as e:
        print(e)
        result['res'] = 'failed'
        return JsonResponse(result)

    result['res'] = 'ok'
    result['data'] = data
    return JsonResponse(result)


def my_event(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid=int(request.GET.get('uid',1))
    try:
        u=User.objects.get(UID__exact=uid)
        revelationList = Revelation.objects.filter(UID__exact=uid)
        eventsList = Events.objects.filter(UID__exact=uid)
        List = []
        for i in revelationList:
            if i.status:
                data = {}
                pics = Revelation_Pic.objects.filter(RID__exact=i.RID)
                picsList = [tools.host + i.img.url for i in pics]
                data['pics'] = picsList
                data['type'] = i.type
                data['ID'] = i.RID
                data['Uname'] = u.Uname
                data['UID'] = u.UID
                data['header'] = tools.host + u.header.url
                data['time'] = i.time
                data['title'] = i.title
                data['text'] = i.text
                data['star'] = i.star
                data['tip_off'] = i.tip_off
                data['isPostByEditor'] = i.isPostByEditor
                data['eventTime'] = tools.stamp2strtime(i.eventTime.timestamp())
                data['mainPic'] = tools.host + Revelation_Pic.objects.filter(RID__exact=i.RID).first().img.url
                List.append(data)
        for i in eventsList:
            if i.status:
                tmp = {}
                tmp['Uname'] = u.Uname
                tmp['UID'] = u.UID
                tmp['header'] = tools.host + u.header.url
                tmp['type'] = 2
                tmp['EID'] = i.EID
                tmp['status'] = i.status
                tmp['Ttitle'] = Topic.objects.get(TID__exact=i.TID).title
                tmp['statement'] = i.statement
                tmp['star'] = i.star
                tmp['tip-off'] = i.tip_off
                tmp['time'] = i.time
                tmp['eventTime']=tools.stamp2strtime(i.eventTime.timestamp())
                tmp['url'] = i.url
                List.append(tmp)
    except Exception as e:
        print(e)
        result['res'] = 'failed'
        return JsonResponse(result)

    result['res'] = 'ok'
    result['data'] = List
    return JsonResponse(result)