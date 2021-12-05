from django.urls import path
from . import views
urlpatterns = [
    path('mainPage', views.info, name='Activity_mainPage'),
    path('show_votes',views.show_Activity_vote,name='show_Activity_vote'),
    path('vote',views.vote,name='Activity_vote'),
    path('star',views.star,name='Activity_star'),
    path('tip-off',views.tip_off,name='Activity_tip_off'),
    path('all',views.all,name='Activity_all'),
    path('show_contributes',views.show_contributes,name='Activity_show_contributes'),

]