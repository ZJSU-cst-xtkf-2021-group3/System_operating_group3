from django.urls import path
from . import views

urlpatterns = [

    path('tip-off',views.Topic_tip_off,name='topic_tip-off'),
    path('star',views.Topic_star,name='topic_star'),
    path('subscribe',views.Subscribe,name='topic_subscribe'),
    path('show_votes',views.show_topic_vote,name='show_topic_vote'),
    path('votes',views.votes,name='votes_topic'),
    path('show_info',views.show_topic_info,name='show_topic_info'),
]