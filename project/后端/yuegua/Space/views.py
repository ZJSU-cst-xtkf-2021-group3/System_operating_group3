import json

from django.http import HttpResponse,HttpResponseRedirect
from models.models import User,userFollow_user
from django.urls import reverse
from django.http import JsonResponse
from Tools import func as tools

def follow_user(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid=request.POST.get('uid')

    F_uid=int(request.GET.get("UID"))

    try:
        usr = User.objects.get(UID__exact=uid)
        Fusr=User.objects.get(UID__exact=F_uid)
        userFollow_user.objects.create(UID=usr.UID,FUID=Fusr.UID,AgeRange=Fusr.AgeRange,FUname=Fusr.Uname,lastVisitTime=tools.getTime())

        #消息通知：



    except Exception as e:
        print(e)
        result['res']='failed'


    return JsonResponse(result)
#
# def see_UserFollowUser(request):
