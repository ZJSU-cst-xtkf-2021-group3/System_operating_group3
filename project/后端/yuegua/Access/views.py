from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from models.models import User
from django.urls import reverse
def check_in(request):
    return HttpResponse("ok")