from django.shortcuts import *
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
from django.db.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic import ListView

import operator

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
            new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
            login(request, new_user)

            return redirect('upd/')
            
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
            user_form.save()
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

# @login_required
# def newevent(request):
#     events = EventForm()
#     return render(request, 'userApp/newevent.html', {'events':events})

@login_required
def newevent(request):
   
    # profile = PersonProfile.objects.get(pk=1)
    # profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
    
    a = EventProfile()
    eventform = EventForm(request.POST)

    if request.method == 'POST':
        #user_form = UserForm(request.POST, instance=request.user)

        if eventform.is_valid():
            #user_defined_code = eventform.cleaned_data.get('user_defined_code')
            #user_form = UserForm(request.POST, instance=request.user)
            #profile_form = ProfileForm(request.POST, instance=request.user.profile)
            
            p_profile = get_object_or_404(PersonProfile, user=request.user)
            p_profile.save()
            doc = eventform.save(commit=False)
            doc.company = p_profile
            doc.save()

            #new_event=eventform.save()
    
            #event = EventProfile.save(commit=False)
            return redirect('/feed/')
        

    else:
        return render(request, 'userApp/newevent.html', {'events':eventform})

def newevent_old(request):
    form=EventForm(request.POST)
    if request.method=='post':
        form=EventForm(request.POST)
        if form.is_valid():
            user_defined_code = form.cleaned_data.get('user_defined_code')
            doc_code = PersonProfile(company=user_defined_code)
            doc_code.save()
            doc = form.save(commit=False)
            doc.code = doc_code
            doc.save()
            
            return HttpResponse('success')
    else:
        form=EventForm()

    context = { 'form':form, }

    return render(request, 'userApp/newevent.html', context)

class MusiciansList(ListView):
    model = PersonProfile
    #paginate_by = 10  # if pagination is desired
    context_object_name = 'musician_list'
    template_name = 'userApp/feed.html'

    def get_queryset(self):
        result = super(MusiciansList, self).get_queryset()
        query = self.request.GET.get('q')
        instrs = self.request.GET.get('instrs')
        genres = self.request.GET.get('genres')

        if (not query):
            query=''
        if(not instrs):
            instrs=''
        if(not genres):
            genres=''
        
        result = PersonProfile.objects.filter(Q(nickname__icontains=query) & Q(instruments__icontains=instrs) & Q(genres__icontains=genres))
        #result = result.filter(Q(nickname__icontains=query) & Q(instruments__icontains=instruments)

        return result

        


def profile(request, person_id):
    persondetail = get_object_or_404(PersonProfile, pk=person_id)
    userdetail = persondetail.user

    return render(request, 'userApp/profile.html', 
    {'profile':persondetail,
    'userprofile':userdetail,
    })


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