from django.urls import path, include
from django.views.generic import ListView, DetailView
from . import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.mainpage , name='mainpage'),
    path('', include('django.contrib.auth.urls')),
    path('reg/', views.registration , name='registration'), 
    #TEMP
    path('feed/', views.feed, name='feed'),
    path('reg/upd/', views.update_profile , name='update_profile'),
    path('<int:person_id>/', views.detail, name="detail"),
    
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


