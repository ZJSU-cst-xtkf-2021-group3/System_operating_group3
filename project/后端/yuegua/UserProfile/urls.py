from django.urls import path
from . import views
urlpatterns = [

    path('setInterests',views.setInterests,name='setInterests'),
    path('modifyName',views.modify_uname,name='modifyName'),
    path('modifyPasswd',views.modify_passwd,name='modifyPasswd'),
    path('modifyHeader',views.modify_header,name='modifyHeader'),
    path('modifyInfo', views.modify_info, name='modifyInfo'),

]