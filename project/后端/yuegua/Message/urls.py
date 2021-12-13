from django.urls import path
from . import views

urlpatterns = [

    path('stars',views.cat_stars,name='cat_stars'),
    path('followers',views.cat_followers,name='cat_followers'),
    path('sysNotes',views.sysNotes,name='sysNotes'),
    path('RTMSG',views.RTMSG,name='RTMSG'),
]