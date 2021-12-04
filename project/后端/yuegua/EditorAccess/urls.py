from django.urls import path
from . import views

urlpatterns = [

    path('login',views.check_in,name='login'),
    path('tip-off',views.manage_tip_off,name='manage_tip_off'),
    # path('userLogout',views.check_out,name="logout")

]