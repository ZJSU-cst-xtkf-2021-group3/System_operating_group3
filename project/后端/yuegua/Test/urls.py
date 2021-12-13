from django.urls import path
from . import views

urlpatterns = [

    path('json',views.receive,name='test_receive_json'),
    path('ite',views.ite),
    path('login',views.check_in),
    path('ping',views.ping),
    path('pic',views.pic),
    path('cache',views.Cache),
    path('cache2',views.Cache2)

]