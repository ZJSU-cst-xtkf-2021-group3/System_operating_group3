from django.urls import path
from . import views
urlpatterns = [

    path('setInterests',views.setInterests,name='setInterests'),

]