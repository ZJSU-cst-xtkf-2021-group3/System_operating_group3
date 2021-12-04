from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
import json
from models.models import Tip_off, User


def ite(request):
    List=Tip_off.objects.all()
    ol=[]
    result={}
    for item in List:
        tmp={}
        tmp['type']=item.type
        tmp['uid']=item.UID
        tmp['valueID']=item.valueID
        ol.append(tmp)
    result['ol']=ol
    result['res']='ok'
    return JsonResponse(result)


def receive(request):
    msg=json.loads(request.body.decode())
    # print(type(msg))
    favList=msg['fav']
    print(favList)
    print(type(favList))
    print(favList[1])

    return HttpResponse("ok")


def ping(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    print("uid:")
    print(uid)
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    else:
        return HttpResponse("no problem")


def check_in(request):
    result = {
        'res': ''
    }

    uname=request.GET.get('username','')
    passwd = request.GET.get('password', '')
    print(uname)
    print(passwd)
    try:
        usr=User.objects.get(Uname__exact=uname)
    except Exception as e:
        print(e)
        result['res']='user not exit'
        return JsonResponse(result)
    if usr.Passwd == passwd:
        request.session['uid'] = usr.UID
        result['res'] = 'check passed'
        return JsonResponse(result)
    else:
        result['res']='check failed'
        return JsonResponse(result)