from django.urls import path
from . import views

urlpatterns = [

    path('login',views.check_in,name='login'),
    path('logout',views.check_out,name='logout'),
    path('register',views.register,name='register')

]