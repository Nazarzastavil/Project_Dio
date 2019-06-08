from django.urls import path, include, re_path
from django.views.generic import ListView, DetailView
from . import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.mainpage , name='mainpage'),
    path('', include('django.contrib.auth.urls')),
    path('reg/', views.registration , name='registration'), 
    path('feed/', views.MusiciansList.as_view(), name='MusiciansList'),
    # re_path(r'feed/(\d+)$',views.EventFollow, name = 'EventFollow'),
    path('feed/updfollow/', views.EventFollowList, name = 'EventFollowList' ),
    path('reg/upd/', views.update_profile , name='update_profile'),
    path('<int:person_id>/', views.profile, name="profile"),
    
    path('follows/<int:pk>', views.follow, name="follow"),
    path('unfollow/<int:pk>', views.unfollow, name="unfollow"),

    path('newevent/', views.newevent, name="newevent"),
    path('feed/search/', views.MusiciansList.as_view(), name="search"),
    path('newgroup/', views.GroupCreate.as_view(), name="newgroup"),
    path('feed/acceptevent/', views.RequestEventAccept, name="EventAccept"),  
    path('newevent/createrequest', views.MusiciansListRequest, name="Req"),
    path('newevent/createevent/', views.EventCreate, name="Req1"),
    
    path('myevents/', views.EventList.as_view(), name="EventList"),
    path('myevents/<int:pk>/', views.EventUpdate.as_view(), name='EventUpdate'),
    path('myevents/<int:pk>/delete/', views.EventDelete.as_view(), name='EventDelete'),

    
    path('users/<int:pk>/', views.UserUpdate.as_view(), name="UserUpdate"),
    # path('users/<int:pk>/', views.UserUpdate, name="UserUpdate"),

    # path('event/add/', views.EventCreate.as_view(), name='event-add'),
    # path('feed/<int:pk>/', views.EventUpdate.as_view(), name='EventUpdate'),

    # re_path(r'feed/(\d+)$',views.EventUpdate.as_view(), name = 'EventUpdate'),
    
    # path('event/<int:pk>/delete/', views.EventDelete.as_view(), name='event-delete'),


    
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


