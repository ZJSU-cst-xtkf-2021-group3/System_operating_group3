from django.urls import path
from . import views

urlpatterns = [

    path('rights',views.seeMy_rights,name='seeMy_rights'),
    path('profile',views.profile,name='profile'),
    path('del/subscribe',views.del_subscribe,name='del_subscribe'),
    path('del/follow',views.del_follow,name='del_follow'),
    path('cat/my/subscribe',views.my_subscribe,name='my_subscribe'),
    path('cat/my/follow',views.my_follow,name='my_my_follow'),
    path('cat/mypost/topics',views.my_topics,name='my_topics'),
    path('cat/mypost/comments',views.my_comments,name='my_topics'),
    path('cat/mypost/events',views.my_event,name='my_topics'),

]
