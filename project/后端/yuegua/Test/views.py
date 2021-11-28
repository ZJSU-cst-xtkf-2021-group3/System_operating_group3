from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
import json

def receive(request):
    msg=json.loads(request.body.decode())
    # print(type(msg))
    favList=msg['fav']
    print(favList)
    print(type(favList))
    print(favList[1])

    return HttpResponse("ok")
