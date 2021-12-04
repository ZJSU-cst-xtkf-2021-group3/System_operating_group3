from django.http import HttpResponse,HttpResponseRedirect
from models.models import User,Comments
from django.urls import reverse
from django.http import JsonResponse
from Tools import func as tools
from models.models import Tip_off,Star


def show_comments(request):
    result={}
    List=[]

    TID=request.GET.get('TID')
    try:
        commentsList=Comments.objects.filter(TID__exact=TID,).order_by('-star')
        for i in commentsList:
            if i.status:
                data={}
                data['CID']=i.CID
                data['UID']=i.UID
                data['Uname']=i.Uname
                data['value']=i.value
                data['time']=tools.stamp2strtime(i.time)
                data['star']=i.star
                data['tip_off']=i.tip_off
                List.append(data)
    except Exception as e:
        print(e)
        result['res']='failed'
        return JsonResponse(result)
    result['data']=List
    result['res'] = 'ok'
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
    cid = int(request.GET.get('CID'))
    try:
        c = Comments.objects.get(CID__exact=cid)
        cu = User.objects.get(UID__exact=c.UID)
        exist = Star.objects.filter(UID__exact=uid, type__exact=4, valueID__exact=cid)
        if exist or c.UID == uid:
            result['res'] = 'refused'
            return JsonResponse(result)

        # add exp
        tools.addEXP(uid, 3)
        tools.addEXP(cu.UID, 3)

        # 通知


        # counts
        c.star += 1
        c.hotPoints = c.hotPoints + 0.1
        c.save()

        # 保存记录
        Star.objects.create(UID=uid, type=4, valueID=cid)
    except Exception as e:
        print(e)
        result['res'] = 'failed'
        return JsonResponse(result)

    result['res'] = 'ok'
    return JsonResponse(result)



def tip_off(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)


    cid = int(request.GET.get('CID'))
    try:
        c = Comments.objects.get(CID__exact=cid)
        Tip_off.objects.create(type=4, valueID=cid, UID=c.UID, points=10)
        c.tip_off += 1
        c.save()

    except Exception as e:
        print(e)
        result['res'] = 'failed'
        return JsonResponse(result)

    result['res'] = "ok"
    return JsonResponse(result)
