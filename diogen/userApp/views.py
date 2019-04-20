from django.shortcuts import render
from django.views.generic import ListView
from userApp.models import Person

#class PersonList(ListView):
#    model = Person

# Create your views here.

def users(request):
    return render(request, 'mainApp/persons.html')