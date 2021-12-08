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
from django.core.paginator import Paginator

def search(request):
    key=request.GET.get("key")
    page = int(request.GET.get("page", 1))
    result={
        'res':'',
        'history':''
    }
    try:
        All=Topic.objects.filter(Q(title__contains=key)|Q(Tag__contains=key),Q(status__exact=True)).order_by('-hotPoints')
        paginator=Paginator(All,10)
        MatchList=paginator.get_page(page)
        if  MatchList.has_next():
            result['has_next'] = 'yes'
        else:
            result['has_next']='no'
            print("ok")

        if  MatchList.has_previous():
            result['has_previous'] = 'yes'
        else:
            result['has_previous'] = 'no'


        data=[]
        for i in MatchList:
            tmp={}
            tmp['TID']=i.TID
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
    result['current_page']=MatchList.number
    return JsonResponse(result)


def rank(request):
    result = {
        'res': '',
    }
    try:
        data=[]
        rankList=Topic.objects.filter(status__exact=True).order_by('-hotPoints')[:10]
        for i in rankList:
            tmp={}
            tmp['TID']=i.TID
            tmp['title']=i.title

            data.append(tmp)
        result['data']=data
        result['res']='ok'
        return JsonResponse(result)

    except Exception as e:
        print(e)
        result['res']='failed'
        return JsonResponse(result)


def category(request):
    result = {
        'res': '',
    }
    C=int(request.GET.get('category'))
    page = int(request.GET.get("page", 1))
    try:
        data=[]
        All=Topic.objects.filter(Q(status__exact=True),Q(category__exact=C)).order_by('-hotPoints')
        paginator=Paginator(All,10)
        rankList=paginator.get_page(page)

        if rankList.has_next():
            result['has_next'] = 'yes'
        else:
            result['has_next']='no'
            print("ok")

        if rankList.has_previous():
            result['has_previous'] = 'yes'
        else:
            result['has_previous'] = 'no'

        for i in rankList:
            tmp={}
            tmp['TID']=i.TID
            tmp['title']=i.title
            tmp['Uname'] = User.objects.get(UID__exact=i.UID).Uname
            tmp['statement'] = i.statement
            tmp['lastUpDateTime'] = tools.stamp2strtime(i.lastUpDateTime)
            tmp['star'] = i.star
            tmp['tip-off'] = i.tip_off
            tmp['Tag'] = i.Tag
            tmp['isPostByEditor'] = i.isPostByEditor
            tmp['Fcounts'] = i.Fcounts

            data.append(tmp)
        result['data']=data
        result['res']='ok'
        result['current_page'] = rankList.number
        return JsonResponse(result)

    except Exception as e:
        print(e)
        result['res']='failed'
        return JsonResponse(result)


def recommend(request):
    result = {
        'res': '',
    }

    uid = request.session.get('uid', -1)

    # uid = request.GET.get('uid')
    if uid != -1:

        try:
            u = User.objects.get(UID__exact=uid)
            data=[]
            rankList=Topic.objects.filter(Q(status__exact=True),Q(AgeRange_avg__exact=u.UID)).order_by('-hotPoints')[:5]
            for i in rankList:
                tmp={}
                tmp['TID']=i.TID
                tmp['title']=i.title
                data.append(tmp)

            lenth=len(data)
            if lenth<5 :
                compensation=Topic.objects.filter(status__exact=True).order_by('-hotPoints')[:5-lenth]
                for i in compensation:
                    tmp = {}
                    tmp['TID'] = i.TID
                    tmp['title'] = i.title
                    data.append(tmp)

            result['data']=data
            result['res']='ok'
            return JsonResponse(result)

        except Exception as e:
            print(e)
            result['res']='failed'
            return JsonResponse(result)
    else:
        result['res'] = 'empty'
        return JsonResponse(result)

def default(request):
    result = {
        'res': '',
    }
    try:
        data = []
        ALl = Topic.objects.filter(Q(status__exact=True)).order_by('-hotPoints')
        page=int(request.GET.get("page",1))
        paginator=Paginator(ALl,10)
        List=paginator.get_page(page)
        if List.has_next():
            result['has_next'] = 'yes'
        else:
            result['has_next']='no'
            print("ok")

        if List.has_previous():
            result['has_previous'] = 'yes'
        else:
            result['has_previous'] = 'no'

        for i in List:
            tmp = {}
            tmp['TID'] = i.TID
            tmp['title'] = i.title
            tmp['Uname'] = User.objects.get(UID__exact=i.UID).Uname
            tmp['statement'] = i.statement
            tmp['lastUpDateTime'] = tools.stamp2strtime(i.lastUpDateTime)
            tmp['star'] = i.star
            tmp['tip-off'] = i.tip_off
            tmp['Tag'] = i.Tag
            tmp['isPostByEditor'] = i.isPostByEditor
            tmp['Fcounts'] = i.Fcounts
            data.append(tmp)
        result['current_page']=List.number
        result['data'] = data
        result['res'] = 'ok'

        return JsonResponse(result)

    except Exception as e:
        print(e)
        result['res'] = 'failed'
        return JsonResponse(result)
