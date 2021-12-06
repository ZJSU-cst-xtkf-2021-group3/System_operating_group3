from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
import json
from Tools import func as tools
from models.models import Topic,User
from django_redis import get_redis_connection
from django.core.cache import cache


def search(request):
    key=request.GET.get("key")
    result={
        'res':'',
        'history':''
    }
    try:
        MatchList=Topic.objects.filter(Q(title__contains=key)|Q(Tag__contains=key),Q(status__exact=True)).order_by('-hotPoints')

        data=[]
        for i in MatchList:
            tmp={}
            tmp['Uname']=User.objects.get(UID__exact=i.UID).Uname
            tmp['title']=i.title
            tmp['statement']=i.statement
            tmp['category']=i.category
            tmp['lastUpDateTime']=tools.stamp2strtime(i.lastUpDateTime)
            tmp['star']=i.star
            tmp['tip-off']=i.tip_off
            tmp['Tag']=i.Tag
            tmp['isPostByEditor']=i.isPostByEditor
            tmp['Fcounts']=i.Fcounts
            data.append(tmp)

        # uid = int(request.session.get('uid', '-1'))
        uid=request.GET.get('uid')
        if uid!=-1:
            if cache.has_key(uid):
                l=cache.get(uid)
                l.append(key)
                cache.set(uid,l,60*10)
                print(l)
                if len(l)==5:
                    l.pop(0)
                    l.append(key)
                    cache.set(uid,l,60*10)
            else:
                l=[]
                l.append(key)
                cache.set(uid,l,60*10)

            result['history'] = cache.get(uid)

    except Exception as e:
        print(e)
        result['res']='failed'
        return JsonResponse(result)

    result['res']="ok"
    result['data']=data
    return JsonResponse(result)