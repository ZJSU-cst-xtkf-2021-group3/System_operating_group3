from django.urls import path
from . import views

urlpatterns = [

    path('topic',views.post_topic,name='post_topic'),
    path('comment',views.post_comment,name='post_comment'),
    path('event',views.post_event,name='post_event'),
    path('revelation',views.post_revelation,name='post_revelation'),
    path('Activity',views.post_Activity,name='post_Activity'),
    path('activity_contribute',views.post_activity_contribute,name='activity_contribute'),


]