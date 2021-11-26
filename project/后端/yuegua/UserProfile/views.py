from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from models.models import userInterests
from django.urls import reverse
from django.http import JsonResponse
# Create your views here.

def setInterests(request):
    result={
        'res':''
    }
    uid = request.session.get('uid', '-1')
    if uid =='-1':
        result['res']='login please'
        return JsonResponse(result)

    if request.method=='POST':
        pass

