from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from models.models import User, Comments
from django.urls import reverse
from django.http import JsonResponse
from Tools import func as tools
from models.models import Tip_off, Star, Events, Revelation,Revelation_Pic


def all(request):
    result = {
        'res': ''
    }
    List=[]
    try:
        tid=int(request.GET.get("TID"))
        eventsList=Events.objects.filter(Q(TID__exact=tid),Q(status__exact=True))
        revelationList=Revelation.objects.filter(Q(TID__exact=tid),Q(status__exact=True))

        for i in eventsList:
            if i.status:
                u=User.objects.get(UID__exact=i.UID)
                data={}
                data['type']=i.type
                data['ID']=i.EID
                data['Uname']=u.Uname
                data['UID']=u.UID
                data['header']=tools.host+u.header.url
                data['time']=i.time
                data['title']=i.title
                data['statement']=i.statement
                data['star']=i.star
                data['tip-off']=i.tip_off
                data['isPostByEditor']=i.isPostByEditor
                data['url']=i.url
                data['eventTime']=i.eventTime.timestamp()
                List.append(data)

        for i in revelationList:
            if i.status:
                u=User.objects.get(UID__exact=i.UID)
                data={}
                pics = Revelation_Pic.objects.filter(RID__exact=i.RID)
                picsList = [tools.host + i.img.url for i in pics]
                data['pics']=picsList
                data['type'] = i.type
                data['ID'] = i.RID
                data['Uname'] = u.Uname
                data['UID']=u.UID
                data['header']=tools.host+u.header.url
                data['time'] = i.time
                data['title'] = i.title
                data['statement'] = i.statement
                data['star'] = i.star
                data['tip-off'] = i.tip_off
                data['isPostByEditor'] = i.isPostByEditor
                data['eventTime'] = i.eventTime.timestamp()
                data['mainPic']=tools.host+Revelation_Pic.objects.filter(RID__exact=i.RID).first().img.url
                List.append(data)

    except Exception as e:
        print(e)
        result['res'] = 'failed'
        return JsonResponse(result)

    List.sort(key= lambda x:x["eventTime"])

    result['data']=List
    result['res']='ok'
    return JsonResponse(result)

def star(request):

    global obj, objU
    result = {
        'res': ''
    }
    uid = request.session.get('uid', -1)
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid = int(request.GET.get('uid'))
    id = int(request.GET.get('ID'))
    type = int(request.GET.get('type'))
    try:
        if type == 2:
            obj = Events.objects.get(EID__exact=id)
            objU = User.objects.get(UID__exact=obj.UID)
        elif type == 3:
            obj = Revelation.objects.get(RID__exact=id)
            objU = User.objects.get(UID__exact=obj.UID)

        exist = Star.objects.filter(UID__exact=uid, type__exact=obj.type, valueID__exact=id)
        if exist or obj.UID == uid:
            result['res'] = 'refused'
            return JsonResponse(result)

        # add exp
        tools.addEXP(uid, 3)
        tools.addEXP(objU.UID, 4)

        # 通知


        # counts
        obj.star += 1
        obj.save()

        # 保存记录
        Star.objects.create(UID=uid, type=obj.type, valueID=id)
    except Exception as e:
        print(e)
        result['res'] = 'failed'
        return JsonResponse(result)

    result['res'] = 'ok'
    return JsonResponse(result)


def tip_off(request):
    global obj
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)

    id = int(request.GET.get('ID'))
    type = int(request.GET.get('type'))
    try:
        if type == 2:
            obj = Events.objects.get(EID__exact=id)
        elif type == 3:
            obj = Revelation.objects.get(RID__exact=id)
        Tip_off.objects.create(type=obj.type, valueID=id, UID=obj.UID, points=20)
        obj.tip_off += 1
        obj.save()

    except Exception as e:
        print(e)
        result['res'] = 'failed'
        return JsonResponse(result)

    result['res'] = "ok"
    return JsonResponse(result)

def show_revelation(request):
    rid=int(request.GET.get("RID"))
    result = {
        'res': ''
    }
    try:
        R=Revelation.objects.get(RID__exact=rid)
        if R.status:
            pics=Revelation_Pic.objects.filter(RID__exact=rid)
            picsList=[tools.host+i.img.url for i in pics]
            tmp={}
            tmp['pics']=picsList
            tmp['text']=R.text
            tmp['ID']=R.RID
            tmp['Uname']=User.objects.get(UID__exact=R.UID).Uname
            tmp['time']=tools.stamp2strtime(R.time)
            tmp['title']=R.title
            tmp['statement']=R.statement
            tmp['star']=R.star
            tmp['tip-off']=R.tip_off
            tmp['isPostByEditor']=R.isPostByEditor
            tmp['eventTime']=R.eventTime.timestamp()
            result['data']=tmp
    except Exception as e:
        print(e)
        result['res']='failed'
        return JsonResponse(result)

    result['res'] = 'ok'
    return JsonResponse(result)
