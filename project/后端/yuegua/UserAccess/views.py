from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from models.models import User
from models.models import userPrivacy
from django.urls import reverse
from django.http import JsonResponse
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
            request.session['uid'] = usr.UID
            result['res'] = 'check passed'
            response=JsonResponse(result)
            response.set_cookie('UID',usr.UID,expires=60 * 60 * 24 * 1)
            return response
        else:
            result['res']='check failed'
            return JsonResponse(result)

def check_out(request):
    result = {
        'res': ''
    }
    try:
        del request.session['uid']
        result['res']='ok'
        response=JsonResponse(result)
        response.delete_cookie('UID')
        return response
    except Exception as e:
        print(e)

def register(request):
    global pic, ageRange
    result={
        'res':''
    }
    if request.method=='POST':
        uname=request.POST.get('username','')
        passwd=request.POST.get('password','')
        age=request.POST.get('age','')
        wechat=request.POST.get('wechat','')
        introduction=request.POST.get('introduction','')
        #头像
        try:
            pic=request.FILES.get('header')
        except Exception as e:
            print(e)
        #年龄段转换

        if not pic:
            pic='/static/img/header_default.png'
        try:
            ageRange=ageSwitch(int(age))
        except Exception as e:
            print(e)

        check=User.objects.filter(Uname__exact=uname)
        if check:
            result['res']='user already exist'
            return JsonResponse(result)
        else:
            try:
                newUser=User.objects.create(Uname=uname,Passwd=passwd,isEDIT=False,header=pic,AgeRange=ageRange,rank=1,
                                    introduction=introduction,wechatID=wechat,EXP=0,Fcounts=0
                                    )
                userPrivacy.objects.create(UID=newUser.UID, public=False, public_Ftopic=True,public_Fuser=True,public_events=True,
                                           public_topics=True,public_comments=True)
            except Exception as e:
                print(e)

            result['res']='ok'
            return JsonResponse(result)

def ageSwitch(age):
    if age>=0 and age<=13:
        return 1
    if age>=14 and age<=17:
        return 2
    if age>=18 and age<=25:
        return 3
    if age >= 26 and age <= 35:
        return 4
    if age >= 36 and age <= 45:
        return 5
    if age >= 46 and age <= 56:
        return 6
    if age>=57:
        return 7
