from django.shortcuts import render, get_object_or_404
from .models import Person
 
def allpersons(request):
    persons = Person.objects
    return render(request, 'userApp/allpersons.html', {'persons':persons})
 
def detail(request, person_id):
    persondetail = get_object_or_404(Person, pk=person_id)
    return render(request, 'userApp/detail.html', {'person':persondetail})