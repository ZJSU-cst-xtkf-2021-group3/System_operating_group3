from django.urls import path
from . import views

urlpatterns = [

    path('all',views.show_comments,name='show_comments'),
    path('star',views.star,name='comments_star'),
    path('tip-off',views.tip_off,name='comments_tip_off'),

    ]