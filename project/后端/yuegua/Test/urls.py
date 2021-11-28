from django.urls import path
from . import views

urlpatterns = [

    path('json',views.receive,name='test_receive_json'),

]