from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from models.models import User
from django.urls import reverse
from django.http import JsonResponse
def check_in(request):
    # result = {
    #     'res': ''
    # }
    # if request.method=='POST':
    #     uname=request.POST.get('username','')
    #     passwd = request.POST.get('password', '')
    #     try:
    #         usr=User.objects.get(Uname__exact=uname)
    #     except Exception as e:
    #         result['res']='user not exit'
    #         return JsonResponse(result)
    #     if usr.Passwd == passwd:
    #         request.session['uid'] = usr.UID
    #         result['res'] = 'check passed'
    #         return JsonResponse(result)
    #     else:
    #         result['res']='check failed'
    #         return JsonResponse(result)
    pass