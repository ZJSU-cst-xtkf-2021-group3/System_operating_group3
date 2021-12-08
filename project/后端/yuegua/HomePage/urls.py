from django.urls import path
from . import views
urlpatterns = [

    path('search',views.search,name='homePage_search'),
    path('rank',views.rank,name='homePage_rank'),
    path('category',views.category,name='homePage_category'),
    path('recommend',views.recommend,name='homePage_recommend'),
    path('default',views.default,name='homePage_default'),


    ]