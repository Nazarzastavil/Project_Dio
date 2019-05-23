from django.urls import path, include, re_path
from django.views.generic import ListView, DetailView
from . import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.mainpage , name='mainpage'),
    path('', include('django.contrib.auth.urls')),
    path('reg/', views.registration , name='registration'), 
    #TEMP
    #re_path(r'^feed/([\w-]+)/$', views.MusiciansList.as_view()),
    path('feed/', views.MusiciansList.as_view(), name='MusiciansList'),
    # path('feed/', views.EventFollow, name='EventFollow'),
    re_path(r'feed/(\d+)$',views.EventFollow, name = 'EventFollow'),
    path('reg/upd/', views.update_profile , name='update_profile'),
    path('<int:person_id>/', views.profile, name="profile"),
    path('newevent/', views.newevent, name="newevent"),
    path('feed/search/', views.MusiciansList.as_view(), name="search")
    
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


