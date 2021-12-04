from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from models.models import User
from django.urls import reverse
from django.http import JsonResponse
from models.models import Tip_off
from models.models import Topic
from models.models import Comments
from models.models import Events
from models.models import Revelation
from Tools import func as tools

def check_in(request):
    result = {
        'res': ''
    }
    if request.method=='POST':
        uname=request.POST.get('username','')
        passwd = request.POST.get('password', '')
        try:
            usr=User.objects.get(Uname__exact=uname)
        except Exception as e:
            result['res']='user not exit'
            return JsonResponse(result)
        if usr.Passwd == passwd:

            if usr.isEDIT==True:
                request.session['uid'] = usr.UID
                result['res'] = 'check passed'
                return JsonResponse(result)

        else:
            result['res']='check failed'
            return JsonResponse(result)


def manage_tip_off(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    if request.method=='GET':
        List = Tip_off.objects.all()
        ol = []
        for item in List:
            tmp = {}
            tmp['type'] = item.type
            tmp['uid'] = item.UID
            tmp['valueID'] = item.valueID
            ol.append(tmp)
        result['ol'] = ol
        result['res'] = 'ok'
        return JsonResponse(result)

    if request.method=='POST':
        vid=int(request.POST.get('vid'))
        try:
            item=Tip_off.objects.get(valueID__exact=vid)
            u=User.objects.get(UID__exact=item.UID)
            if item.type==1:
                t=Topic.objects.get(TID__exact=item.valueID)
                t.status=False
                u.EXP-=item.points
                t.save()
                u.save()
                u.rank=tools.exp2rank(u.EXP)
                u.save()
            if item.type==2:
                e=Events.objects.get(EID__exact=item.valueID)
                e.status=False
                u.EXP-=item.points
                e.save()
                u.save()
                u.rank = tools.exp2rank(u.EXP)
                u.save()
            if item.type==3:
                r=Revelation.objects.get(RID__exact=item.valueID)
                r.status=False
                u.EXP-=item.points
                r.save()
                u.save()
                u.rank = tools.exp2rank(u.EXP)
                u.save()
            if item.type==4:
                c = Comments.objects.get(CID__exact=item.valueID)
                c.status=False
                u.EXP -= item.points
                c.save()
                u.save()
                u.rank = tools.exp2rank(u.EXP)
                u.save()


        except Exception as e:
            print(e)
