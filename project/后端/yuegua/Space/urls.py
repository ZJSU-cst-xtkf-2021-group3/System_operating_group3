from django.urls import path
from . import views

urlpatterns = [

    path('follow',views.follow_user,name='follow_user'),
    path('cat/others/Fuserlist',views.others_Fuser,name='others_Fuser'),
    path('cat/others/Ftopiclist',views.others_Ftopic,name='others_Ftopic'),
    path('cat/others/Ptopiclist',views.others_Ptopic,name='others_Ptopic'),
    path('cat/others/Peventlist',views.others_Pevent,name='others_Pevent'),
    path('cat/others/Pcommentlist',views.others_Pcomment,name='others_Pcomment')

]


