from django.urls import path
from . import views
urlpatterns = [

    path('all',views.all,name='show_events'),
    path('star',views.star,name='events_star'),
    path('tip-off',views.tip_off,name='events_tip_off'),
    path('show_revelation',views.show_revelation,name='show_revelation'),

    ]