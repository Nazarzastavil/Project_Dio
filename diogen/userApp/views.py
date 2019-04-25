from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Person
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import datetime
from django.utils.timezone import utc


#def registration(request):
#    return render(request, 'userApp/reg.html')

def allpersons(request):
    persons = Person.objects
    return render(request, 'userApp/allpersons.html', {'persons':persons})
 
def detail(request, person_id):
    persondetail = get_object_or_404(Person, pk=person_id)
    return render(request, 'userApp/detail.html', {'person':persondetail})

from .forms import PersonForm

def registration(request):
    if request.method == "POST":
        name = request.POST.get("name")
        #registertime = request.POST.get("registertime")
        date = request.POST.get("date")
        password = request.POST.get("password")
        spec = request.POST.get("spec")
        image= request.POST.get("image")
        p = Person()
        p.name=name
        p.registertime=datetime.datetime.utcnow().replace(tzinfo=utc)
        p.date=date
        p.spec=spec
        p.phone=1337
        p.description='description'
        p.email='nu da'
        p.clean()
        p.image=image

        p.save()
        # age = request.POST.get("age")     # получение значения поля age
        return HttpResponse("<h2>Hello, {0}</h2>".format(name))
    else:
        personform = PersonForm()
        return render(request, "userApp/reg.html", {"form": personform})

def login(request):
    pass
