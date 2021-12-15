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
    }
    try:
        All=Topic.objects.filter(Q(title__contains=key)|Q(Tag__contains=key),Q(status__exact=True)).order_by('-hotPoints')
        paginator=Paginator(All,5)
        MatchList=paginator.get_page(page)
        if  MatchList.has_next():
            result['has_next'] = 'yes'
        else:
            result['has_next']='no'


        if  MatchList.has_previous():
            result['has_previous'] = 'yes'
        else:
            result['has_previous'] = 'no'


        data=[]
        for i in MatchList:
            u=User.objects.get(UID__exact=i.UID)
            tmp={}
            tmp['TID']=i.TID
            tmp['Uname']=u.Uname
            tmp['title']=i.title
            tmp['statement']=i.statement
            tmp['category']=i.category
            tmp['lastUpDateTime']=i.lastUpDateTime
            tmp['star']=i.star
            tmp['tip_off']=i.tip_off
            tmp['Tag']=i.Tag
            tmp['isPostByEditor']=i.isPostByEditor
            tmp['Fcounts']=i.Fcounts
            tmp['mainPic']=tools.host+i.mainPic.url
            tmp['header']=tools.host+u.header.url
            data.append(tmp)


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
        paginator=Paginator(All,5)
        rankList=paginator.get_page(page)

        if rankList.has_next():
            result['has_next'] = 'yes'
        else:
            result['has_next']='no'


        if rankList.has_previous():
            result['has_previous'] = 'yes'
        else:
            result['has_previous'] = 'no'

        for i in rankList:
            u=User.objects.get(UID__exact=i.UID)
            tmp={}
            tmp['TID']=i.TID
            tmp['title']=i.title
            tmp['Uname'] = u.Uname
            tmp['statement'] = i.statement
            tmp['lastUpDateTime'] = i.lastUpDateTime
            tmp['star'] = i.star
            tmp['tip_off'] = i.tip_off
            tmp['Tag'] = i.Tag
            tmp['isPostByEditor'] = i.isPostByEditor
            tmp['Fcounts'] = i.Fcounts
            tmp['mainPic']=tools.host+i.mainPic.url
            tmp['header'] = tools.host + u.header.url

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
            rankList=Topic.objects.filter(Q(status__exact=True),Q(AgeRange_avg__exact=u.UID)).order_by('-hotPoints')[:10]
            for i in rankList:
                u2=User.objects.get(UID__exact=i.UID)
                tmp={}
                tmp['TID'] = i.TID
                tmp['title'] = i.title
                tmp['Uname'] = u2.Uname
                tmp['statement'] = i.statement
                tmp['star'] = i.star
                tmp['lastUpDateTime'] = i.lastUpDateTime
                tmp['tip_off'] = i.tip_off
                tmp['Tag'] = i.Tag
                tmp['Fcounts'] = i.Fcounts
                tmp['mainPic'] = tools.host + i.mainPic.url
                tmp['header'] = tools.host + u2.header.url

                data.append(tmp)

            lenth=len(data)
            if lenth<10 :
                compensation=Topic.objects.filter(status__exact=True).order_by('-hotPoints')[:10-lenth]
                for i in compensation:
                    u2 = User.objects.get(UID__exact=i.UID)
                    tmp = {}
                    tmp['TID'] = i.TID
                    tmp['title'] = i.title
                    tmp['Uname'] = u2.Uname
                    tmp['statement'] = i.statement
                    tmp['star'] = i.star
                    tmp['lastUpDateTime'] = i.lastUpDateTime
                    tmp['tip_off'] = i.tip_off
                    tmp['Tag'] = i.Tag
                    tmp['Fcounts'] = i.Fcounts
                    tmp['mainPic'] = tools.host + i.mainPic.url
                    tmp['header'] = tools.host + u2.header.url
                    data.append(tmp)

            result['data']=data
            result['res']='ok'
            return JsonResponse(result)

        except Exception as e:
            print(e)
            result['res']='failed'
            return JsonResponse(result)
    else:
        data=[]
        try:
            default = Topic.objects.filter(status__exact=True).order_by('-hotPoints')[:10]
            for i in default:
                u2 = User.objects.get(UID__exact=i.UID)
                tmp = {}
                tmp['TID'] = i.TID
                tmp['title'] = i.title
                tmp['Uname'] = u2.Uname
                tmp['statement'] = i.statement
                tmp['star'] = i.star
                tmp['lastUpDateTime'] = i.lastUpDateTime
                tmp['tip_off'] = i.tip_off
                tmp['Tag'] = i.Tag
                tmp['Fcounts'] = i.Fcounts
                tmp['mainPic'] = tools.host + i.mainPic.url
                tmp['header'] = tools.host + u2.header.url
                data.append(tmp)
        except Exception as e:
            print(e)
            result['res'] = 'failed'
            return JsonResponse(result)

        result['data'] = data
        result['res'] = 'ok'
        return JsonResponse(result)

def default(request):
    result = {
        'res': '',
    }
    try:
        data = []
        ALl = Topic.objects.filter(Q(status__exact=True)).order_by('-hotPoints')
        page=int(request.GET.get("page",1))
        paginator=Paginator(ALl,5)
        List=paginator.get_page(page)
        if List.has_next():
            result['has_next'] = 'yes'
        else:
            result['has_next']='no'


        if List.has_previous():
            result['has_previous'] = 'yes'
        else:
            result['has_previous'] = 'no'

        for i in List:
            u = User.objects.get(UID__exact=i.UID)
            tmp = {}
            tmp['TID'] = i.TID
            tmp['title'] = i.title
            tmp['Uname'] = User.objects.get(UID__exact=i.UID).Uname
            tmp['statement'] = i.statement
            tmp['lastUpDateTime'] = i.lastUpDateTime
            tmp['star'] = i.star
            tmp['tip_off'] = i.tip_off
            tmp['Tag'] = i.Tag
            tmp['isPostByEditor'] = i.isPostByEditor
            tmp['Fcounts'] = i.Fcounts
            tmp['mainPic']=tools.host+i.mainPic.url
            tmp['header'] = tools.host + u.header.url
            data.append(tmp)
        result['current_page']=List.number
        result['data'] = data
        result['res'] = 'ok'

        return JsonResponse(result)

    except Exception as e:
        print(e)
        result['res'] = 'failed'
        return JsonResponse(result)
