from django.shortcuts import *
from .models import *
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse,HttpRequest
from django.urls import reverse,reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import datetime
from django.utils.timezone import utc

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.messages import constants as messages
from django.contrib.auth.forms import UserCreationForm
from userApp.forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.db.models import * 

import operator
import json

def mainpage(request):

    return redirect('login/')

def registration(request):
    print('da')
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
            
            # return HttpResponse('nani!!!')
            # return render(request, 'userApp/reg.html', {'form': form1})
  
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
        print('da')

        if user_form.is_valid() and profile_form.is_valid():
            #profile = PersonProfile(image = request.FILES['image'])

            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            user_form.save()
 
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
  


def newevent(request):
    events = Event()
    return render(request, 'userApp/newevent.html', {'events':events})

class MusiciansList(ListView):
    model = PersonProfile
    #paginate_by = 10  # if pagination is desired
    context_object_name = 'context'
    template_name = 'userApp/feed.html'

    # def get_queryset(self):
        
    #     return result

    def get_context_data(self, **kwargs):
        result = super(MusiciansList, self).get_queryset()
        query = self.request.GET.get('q')
        
        instrs = self.request.GET.get('instrs')
        genres = self.request.GET.get('genres')
        date = self.request.GET.get('date')
        if (not query):
            query=''
        if(not instrs):
            instrs=''
        if(not genres):
            genres=''

        result = PersonProfile.objects.filter(Q(nickname__icontains=query) & Q(instruments__icontains=instrs) 
            & Q(genres__icontains=genres))
 
        context = super(MusiciansList, self).get_context_data(**kwargs)
        context.update({  
            'event_list': EventProfile.objects.all().order_by('date'), 
            'musician_list': result, 
            'event_follows': Participation.objects.filter(userProfile=get_object_or_404(PersonProfile, user=self.request.user)),
            #'current_events': EventProfile.objects.filter(pk=[i.id for i in context['event_follows']], date=date)
        })
        context.update({
             
            'selected_events': EventProfile.objects.filter(pk__in=[i.event.id for i in context['event_follows']], date=date)
        })
        # print([i.pk for i in context['selected_events']]) 
        return context 

def EventFollowList(request):
    # print(request.POST["id"]) 
    event_id = request.POST["id"]
    response_data = {}
    response_data["id"] = event_id
    if request.method == 'POST':
        
        if(Participation.objects.filter(event=event_id).count()==0):
            p = Participation()
            p.userProfile = get_object_or_404(PersonProfile, user=request.user)
            p.is_mus=False
            p.event=get_object_or_404(EventProfile, id=event_id)
            p.save()
            
            response_data["followed"] = True
        else:
            p = get_object_or_404(Participation, event=event_id)
            p.delete() 
            response_data["followed"] = False
    return JsonResponse(response_data)


def EventFollow(request, event_id):
    if request.method == 'POST':
        
        if(Participation.objects.filter(event=event_id).count()==0):
            p = Participation()
            p.userProfile = get_object_or_404(PersonProfile, user=request.user)
            p.is_mus=False
            p.event=get_object_or_404(EventProfile, id=event_id)
            p.save()
            
            response_data["followed"] = True
        else:
            p = get_object_or_404(Participation, event=event_id)
            p.delete()
            response_data["followed"] = False
    return redirect('/feed/')


def profile(request, person_id): #detail view of profile
    persondetail = get_object_or_404(PersonProfile, pk=person_id)
    #persondetail.email=''
    userdetail = persondetail.user

    return render(request, 'userApp/profile.html', 
    {'profile':persondetail,
    'userprofile':userdetail,
    })


class GroupCreate(CreateView):
    model = GroupProfile
    template_name = 'userApp/newgroup.html'
    form_class = GroupForm
    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return redirect('/feed/')
    
    # print(fields)

class EventList(ListView):
    model = EventProfile
    context_object_name = 'context'
    template_name = 'userApp/my_events.html'
    def get_queryset(self):
        result = super(EventList, self).get_queryset()
        return result.filter(company=get_object_or_404(PersonProfile, user=self.request.user))


# class EventCreate(CreateView):
#     model = EventProfile
#     fields = ['name']
   
@login_required
def newevent(request):
   
    # profile = PersonProfile.objects.get(pk=1)
    # profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
    
    a = EventProfile()
    eventform = EventForm(request.POST)

    if request.method == 'POST':

        if eventform.is_valid():
           
            p_profile = get_object_or_404(PersonProfile, user=request.user)
            p_profile.save()
            doc = eventform.save(commit=False)
            doc.company = p_profile
            doc.save()
            return redirect('/myevents/')
    else:
        return render(request, 'userApp/newevent.html', {'events':eventform})


class EventUpdate(UpdateView):
    model = EventProfile
    fields = ['name','date','address','group','description']
    
    def form_valid(self, form):
        
        post = form.save(commit=False)
        post.save()
        return redirect('/myevents/')

    
class EventDelete(DeleteView):
    model = EventProfile
    success_url = '/myevents/'


def EditProfile(request):
    user_form = UserForm(request.POST, instance=request.user)
    profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
    
    
    if request.method == 'POST':

        if user_form.is_valid() and profile_form.is_valid():
            #profile = PersonProfile(image = request.FILES['image'])

            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            user_form.save()

            return redirect('/feed/')

    return render(request, 'userApp/reg.html', {
    'user_form': user_form,
    'profile_form': profile_form,
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