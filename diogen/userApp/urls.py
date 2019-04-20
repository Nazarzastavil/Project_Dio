from django.urls import path, include
from django.views.generic import ListView, DetailView
from userApp.models import Person
from . import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.allpersons , name='allpersons'),
    path('<int:person_id>/', views.detail, name="detail"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

#urlpatterns = [
    #path('',PersonList.as_view())

    #path('', ListView.as_view(queryset=Person.objects.all().order_by("-registertime")[:5],template_name="userApp/persons.html")),

    #path('', views.home, name='home'),
    #path('<int:id>/', views.single, name='single'),

    #path(r'/test', DetailView(model = Person, template_name = "userApp/person.html")),
    #path(r'^(?P<pk>\d+)$', DetailView(model = Person, template_name = "userApp/person.html")),
    #path('test/', views.test, name='test'),
#]

