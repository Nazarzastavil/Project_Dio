from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from .models import *
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import datetime
from django.utils.timezone import utc

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.messages import constants as messages
from django.contrib.auth.forms import UserCreationForm
from userApp.forms import *
from django.contrib.auth import authenticate, login

def mainpage(request):
    return redirect('login/')

def registration(request):
    if request.method == 'POST':
        form1=ProfileForm
        #userform=UserForm
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #messages.success(request, 'Account created successfully')

            #TEMP: логин сразу после регистрации
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            #user_form = UserForm(request.POST, instance=request.user)
            #profile_form = ProfileForm(request.POST, instance=request.user.profile)
            return redirect('upd/')
            
            # return render(request, 'userApp/reg.html', {
            #     'user_form': user_form,
            #     'profile_form': profile_form,
            #     # 'musician_form': musician_form,
            #     # 'company_form': company_form,
            # })
        else:
            pass
            #TEMP
            
            return HttpResponse('nani!!!')
            #return render(request, 'userApp/reg.html', {'form': form1})
    else:
        form = UserCreationForm()
        return render(request, 'userApp/create_user.html', {'form': form})



@transaction.atomic
@login_required
def update_profile(request):
    user_form = UserForm(request.POST, instance=request.user)
    profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
    if request.method == 'POST':
        #user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        

        if user_form.is_valid() and profile_form.is_valid():
            #profile = PersonProfile(image = request.FILES['image'])

            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            #user_form.save()
            #profile_form.save()

            #return redirect('settings:profile')
            #return HttpResponse('success!')
            return redirect('/feed/')

    else:
        return render(request, 'userApp/reg.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        })
    #return HttpResponse('test!')
    #TEMP
  

@login_required
def feed(request):
    persons = PersonProfile.objects
    return render(request, 'userApp/feed.html',{'persons':persons})


def allpersons(request):
    persons = PersonProfile.objects
    return render(request, 'userApp/allpersons.html', {'persons':persons})
 
def detail(request, person_id):
    persondetail = get_object_or_404(PersonProfile, pk=person_id)
    return render(request, 'userApp/detail.html', {'person':persondetail})


'''
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
'''