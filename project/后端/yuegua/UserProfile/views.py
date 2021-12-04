from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from models.models import userInterests
from django.urls import reverse
from models.models import User
from UserAccess.views import ageSwitch
from django.http import JsonResponse
import json

def setInterests(request):
    result={
        'res':''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid ==-1:
        result['res']='login please'
        return JsonResponse(result)

    if request.method=='POST':
        msg = json.loads(request.body.decode())
        favList = msg.get('fav')
        oldList=userInterests.objects.filter(UID__exact=uid)
        oldList.delete()

        try:
            for item in favList:
                userInterests.objects.create(UID=uid,field=int(item))
        except Exception as e:
            print(e)
            result['res'] = "failed"
            return JsonResponse(result)

        result['res']="ok"
        return JsonResponse(result)


def modify_uname(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid ==-1:
        result['res']='login please'
        return JsonResponse(result)
    # uid=request.POST.get('uid')
    usr=User.objects.get(UID__exact=uid)
    newName=request.POST.get('username')
    same=User.objects.filter(Uname__exact=newName)
    if same:
        result['res'] = 'user already exist'
        return JsonResponse(result)
    else:
        usr.Uname=newName
        usr.save()
        result['res'] = 'ok'
        return JsonResponse(result)


def modify_passwd(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid=request.POST.get('uid')
    usr = User.objects.get(UID__exact=uid)
    newPasswd = request.POST.get('password')
    usr.Passwd=newPasswd
    usr.save()
    result['res']='ok'
    return JsonResponse(result)

def modify_header(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid=request.POST.get('uid')
    usr = User.objects.get(UID__exact=uid)
    try:
        newHeader = request.FILES.get('header')
        usr.Header = newHeader
        usr.save()
    except Exception as e:
        print(e)
        result['res'] = 'failed'
        return JsonResponse(result)

    result['res'] = 'ok'
    return JsonResponse(result)


def modify_info(request):
    result = {
        'res': ''
    }
    uid = request.session.get('uid', -1)
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid=request.POST.get('uid')
    usr = User.objects.get(UID__exact=uid)
    try:
        age = request.POST.get('age', '')
        wechat = request.POST.get('wechat', '')
        introduction = request.POST.get('introduction', '')
        age_format=ageSwitch(int(age))
        usr.AgeRange=age_format
        usr.wechatID=wechat
        usr.introduction=introduction
        usr.save()

    except Exception as e:
        print(e)
        result['res'] = 'failed'
        return JsonResponse(result)

    result['res'] = 'ok'
    return JsonResponse(result)