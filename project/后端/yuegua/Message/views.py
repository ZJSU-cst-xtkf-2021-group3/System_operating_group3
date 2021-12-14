from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
import json
from django.core.cache import cache
from models.models import User,Star,userFollow_user,message
import Tools.func as tools


# Create your views here.
def cat_stars(request):
    result={}
    data=[]
    uid = int(request.session.get('uid', '-1'))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    try:
        records=Star.objects.filter(valueID__exact=uid)
        for i in records:
            tmp={}
            u = User.objects.get(UID__exact=i.UID)
            tmp['msg']=u.Uname+" 点赞了您发表的"+tools.switchType(i.type)
            tmp['time']=tools.stamp2strtime(tools.getTime())
            tmp['header']=tools.host+u.header.url
            data.append(tmp)
    except Exception as e:
        print(e)
        result['res']='failed'
        return JsonResponse(result)

    result['data']=data
    result['res']='ok'
    return JsonResponse(result)

def cat_followers(request):
    result = {}
    data = []
    uid = int(request.session.get('uid', '-1'))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    try:
        flist=userFollow_user.objects.filter(FUID__exact=uid)
        for i in flist:
            u=User.objects.get(UID__exact=i.UID)
            tmp={}
            tmp['uname']=u.Uname
            tmp['header']=tools.host+u.header.url
            tmp['introduction']=u.introduction
            data.append(tmp)
    except Exception as e:
        print(e)
        result['res'] = 'failed'
        return JsonResponse(result)

    result['data'] = data
    result['res'] = 'ok'
    return JsonResponse(result)


def sysNotes(request):
    result = {}
    data = []
    uid = int(request.session.get('uid', '-1'))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    try:
       nlist=message.objects.filter(UID__exact=uid)
       for i in nlist:
           tmp={}
           tmp['type']=i.type
           tmp['value']=i.value
           tmp['typeID']=i.typeID
           tmp['postTime']=i.postTime
           data.append(tmp)
       data.sort(key=lambda x:x['postTime'],reverse=True)

    except Exception as e:
        print(e)
        result['res'] = 'failed'
        return JsonResponse(result)

    result['data'] = data
    result['res'] = 'ok'
    return JsonResponse(result)


def RTMSG(request):
    result={}
    data=[]
    tokenList=['Fbot','Ftopic','Nevent','Ncomment','Nfollower']
    uid = int(request.session.get('uid', '-1'))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    for t in tokenList:
        token=str(uid)+t
        if cache.has_key(token):
            value=cache.get(token)
            data.append(value)

    result['data'] = data
    if data==[]:
        result['isEmpty']=True
    else:
        result['isEmpty'] = False
    result['res'] = 'ok'
    return JsonResponse(result)