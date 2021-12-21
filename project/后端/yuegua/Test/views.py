from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
import json
from django.core.cache import cache

from django.views import static

from models.models import Tip_off, User
from django_redis import get_redis_connection


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
        u=User.objects.get(UID__exact=uid)
        result['res'] = u.Uname+" ok"

        return JsonResponse(result)


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

def pic(request):
    u=User.objects.get(UID__exact=1)
    return HttpResponse(u.header)

def Cache(request):
    result={}
    uid = int(request.session.get('uid', 'x'))
    if uid == 'x':
        result['res'] = 'login please'
        return JsonResponse(result)

    if request.method=="POST":
        token = str(uid) + 'notify'
        if cache.has_key(token):
            l = list(cache.get(token))
            l.append("xxx 点赞了你的微博")
            cache.set(token, l, 10)
            print(l)
            if len(l) >3:
                l.pop(0)
                cache.set(token, l, 10)
        else:
            l = []
            l.append("xxx 点赞了你的微博")
            cache.set(token, l, 10)
        result['res']='ok'
        return JsonResponse(result)

    if request.method=='GET':
        uid = int(request.session.get('uid', 'x'))
        if uid == 'x':
            result['res'] = 'login please'
            return JsonResponse(result)
        token = str(uid) + 'notify'
        if cache.has_key(token):
            l = list(cache.get(token))
            result['data']=l

        else:
            result['data']="empty"

        result['res'] = "ok"
        return JsonResponse(result)

def Cache2(request):
    result = {}
    # uid = int(request.session.get('uid', 'x'))
    uid=request.GET.get('uid','x')
    if uid == 'x':
        result['res'] = 'login please'
        return JsonResponse(result)

    token = str(uid) + 'Fbot'
    cache.set(token,"您关注的博主zzz更新啦！", 21)
    token2 = str(uid) + 'Nevent'
    cache.set(token2,"北京冬奥进行时话题有新结点啦！",21)

    result['res'] = 'ok'
    return JsonResponse(result)