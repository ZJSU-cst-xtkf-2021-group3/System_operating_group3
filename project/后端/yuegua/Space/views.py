import json

from django.db.models import Q
from django.http import HttpResponse,HttpResponseRedirect
from models.models import User,userFollow_user,userPrivacy,userFollow_topic,Topic,Revelation,Events,Comments,Revelation_Pic
from django.urls import reverse
from django.http import JsonResponse
from Tools import func as tools
from django.core.cache import cache

def follow_user(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid=int(request.GET.get('uid'))

    F_uid=int(request.GET.get("UID"))
    if F_uid==uid:
        result['res']='refused'
        return JsonResponse(result)


    try:

        check=userFollow_user.objects.filter(Q(UID__exact=uid),Q(FUID__exact=F_uid))
        if check:
            result['res'] = 'refused'
            return JsonResponse(result)
        else:
            usr = User.objects.get(UID__exact=uid)
            Fusr=User.objects.get(UID__exact=F_uid)
            userFollow_user.objects.create(UID=usr.UID,FUID=Fusr.UID,AgeRange=Fusr.AgeRange,FUname=Fusr.Uname,lastVisitTime=tools.getTime())
            tools.addEXP(usr.UID,3)
            tools.addEXP(Fusr.UID,5)
            Fusr.Fcounts+=1
            Fusr.save()

            #消息通知：
            token = str(F_uid) + 'Nfollower'
            cache.set(token, usr.Uname+"成为了您的新粉丝", 21)


    except Exception as e:
        print(e)
        result['res']='failed'

    result['res']='ok'
    return JsonResponse(result)

def others_Fuser(request):
    result = {
        'res': ''
    }

    target_uid = int(request.GET.get("UID"))
    try:
        tup=userPrivacy.objects.get(UID__exact=target_uid)
        if tup.public_Fuser:
            list=userFollow_user.objects.filter(UID__exact=target_uid)
            data=[]
            for i in list:
                tmp_u=User.objects.get(UID__exact=i.FUID)
                tmp={}
                tmp['UID']=i.FUID
                tmp['Uname']=tmp_u.Uname
                tmp['header']=tools.host+tmp_u.header.url
                tmp['Fcounts']=tmp_u.Fcounts
                data.append(tmp)
        else:
            result['res'] = 'refused'
            return JsonResponse(result)

    except Exception as e:
        print(e)
        result['res']='failed'
        return JsonResponse(result)

    result['res']='ok'
    result['data']=data
    return JsonResponse(result)


def others_Ftopic(request):
    result = {
        'res': ''
    }

    target_uid = int(request.GET.get("UID"))
    try:
        tup=userPrivacy.objects.get(UID__exact=target_uid)
        if tup.public_Ftopic:
            list=userFollow_topic.objects.filter(UID__exact=target_uid)
            data=[]
            for i in list:
                tmp_t=Topic.objects.get(TID__exact=i.FTID)
                tu=User.objects.get(UID__exact=tmp_t.UID)
                if tmp_t.status:
                    tmp={}
                    tmp['Uname']=tu.Uname
                    tmp['header']=tools.host+tu.header.url
                    tmp['TID']=i.FTID
                    tmp['Tag']=tmp_t.Tag
                    tmp['Fcounts']=tmp_t.Fcounts
                    tmp['title']=tmp_t.title
                    tmp['statement']=tmp_t.statement
                    tmp['star']=tmp_t.star
                    tmp['tip_off']=tmp_t.tip_off
                    tmp['hotPoints']=tmp_t.hotPoints
                    tmp['mainPic']=tools.host+tmp_t.mainPic.url
                    tmp['lastUpDateTime']=tmp_t.lastUpDateTime
                    data.append(tmp)
        else:
            result['res'] = 'refused'
            return JsonResponse(result)

    except Exception as e:
        print(e)
        result['res']='failed'
        return JsonResponse(result)

    result['res']='ok'
    result['data']=data
    return JsonResponse(result)


def others_Ptopic(request):
    result = {
        'res': ''
    }

    target_uid = int(request.GET.get("UID"))
    try:
        tup = userPrivacy.objects.get(UID__exact=target_uid)
        if tup.public_topics:
            tu=User.objects.get(UID__exact=target_uid)
            list = Topic.objects.filter(UID__exact=target_uid)
            data = []
            for i in list:
                if i.status:
                    tmp = {}
                    tmp['TID'] = i.TID
                    tmp['title'] = i.title
                    tmp['statement'] = i.statement
                    tmp['hotPoints']=i.hotPoints
                    tmp['lastUpDateTime']=i.lastUpDateTime
                    tmp['mainPic']=tools.host+i.mainPic.url
                    tmp['star'] = i.star
                    tmp['Fcounts'] = i.Fcounts
                    tmp['tip_off'] = i.tip_off
                    tmp['Uname']=tu.Uname
                    tmp['header']=tools.host+tu.header.url
                    tmp['Tag']=i.Tag
                    data.append(tmp)
        else:
            result['res'] = 'refused'
            return JsonResponse(result)

    except Exception as e:
        print(e)
        result['res'] = 'failed'
        return JsonResponse(result)

    result['res'] = 'ok'
    result['data'] = data
    return JsonResponse(result)


def others_Pevent(request):
    result = {
        'res': ''
    }

    target_uid = int(request.GET.get("UID"))
    try:
        tup = userPrivacy.objects.get(UID__exact=target_uid)
        if tup.public_events:
            revelationList=Revelation.objects.filter(Q(status=True),Q(UID__exact=target_uid))
            eventsList=Events.objects.filter(Q(status=True),Q(UID__exact=target_uid))
            data = []
            for i in revelationList:
                if i.status:
                    tmp = {}
                    tmp['type']=3
                    tmp['RID'] = i.RID
                    tmp['Ttitle']=Topic.objects.get(TID__exact=i.TID).title
                    tmp['title'] = i.title
                    tmp['statement'] = i.statement
                    tmp['star'] = i.star
                    tmp['tip-off']=i.tip_off
                    tmp['time']=tools.stamp2strtime(i.time)
                    tmp['mainPic'] = tools.host+Revelation_Pic.objects.filter(RID__exact=i.RID).first().img.url
                    data.append(tmp)
            for i in eventsList:
                if i.status:
                    tmp = {}
                    tmp['type'] = 2
                    tmp['EID'] = i.EID
                    tmp['Ttitle'] = Topic.objects.get(TID__exact=i.TID).title
                    tmp['statement'] = i.statement
                    tmp['star'] = i.star
                    tmp['tip-off'] = i.tip_off
                    tmp['time'] = tools.stamp2strtime(i.time)
                    tmp['url'] = i.url
                    data.append(tmp)

        else:
            result['res'] = 'refused'
            return JsonResponse(result)

    except Exception as e:
        print(e)
        result['res']='failed'
        return JsonResponse(result)

    result['data']=data
    result['res']='ok'
    return JsonResponse(result)


def others_Pcomment(request):
    result = {
        'res': ''
    }

    target_uid = int(request.GET.get("UID"))
    try:
        tup = userPrivacy.objects.get(UID__exact=target_uid)
        if tup.public_comments:
            list = Comments.objects.filter(UID__exact=target_uid)
            data = []
            for i in list:
                if i.status:
                    tmp = {}
                    tmp['Ttitle'] = Topic.objects.get(TID__exact=i.TID).title
                    tmp['CID']=i.CID
                    tmp['value'] = i.value
                    tmp['hotPoints'] = i.hotPoints
                    tmp['time'] = tools.stamp2strtime(i.time)
                    tmp['star'] = i.star
                    tmp['tip-off']=i.tip_off
                    data.append(tmp)
        else:
            result['res'] = 'refused'
            return JsonResponse(result)

    except Exception as e:
        print(e)
        result['res'] = 'failed'
        return JsonResponse(result)

    result['res'] = 'ok'
    result['data'] = data
    return JsonResponse(result)


def basicInfo(request):
    result = {
        'res': '',
        'isFouse' : False
    }
    uid = int(request.GET.get('UID'))
    myuid=int(request.session.get('uid','-1'))
    if myuid=="-1":
        result['isFouse']=False
    else:
        try:
            if userFollow_user.objects.filter(Q(UID__exact=myuid),Q(FUID__exact=uid)):
                result['isFouse']=True

        except Exception as e:
            print(e)
            result['res']='failed'
            return JsonResponse(result)
    try:
        u = User.objects.get(UID__exact=uid)
        data = {}
        data['EXP'] = u.EXP
        data['rank'] = u.rank
        data['ifPassedExam'] = u.ifPassedExam
        data['Fcounts'] = u.Fcounts
        data['isEditor'] = u.isEDIT
        data['header'] = tools.host + u.header.url
        data['introduction'] = u.introduction
        data['Uname'] = u.Uname

    except Exception as e:
        print(e)
        result['res'] = 'failed'
        return JsonResponse(result)

    result['res'] = 'ok'
    result['data'] = data
    return JsonResponse(result)
