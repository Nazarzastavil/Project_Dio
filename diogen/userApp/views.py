from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
 
from  userApp.models import Person
 
 
def home(request):
    #personList = Person.objects.filter(spec='1')
    personList = Person.objects
    paginator = Paginator(personList, 4)
    page = request.GET.get('page')
    querysetGoods = paginator.get_page(page)
 
    context = {
        "persons": personList,
        "description": "Описание",
    }
    return render(request, "userApp/home.html", context)
 
def single(request, id=None):
    person = get_object_or_404(Person, id=id)
 
    context = {
        "person": person,
    }
    return render(request, "userApp/single.html", context)


def users(request):
    return render(request, 'userApp/persons.html')