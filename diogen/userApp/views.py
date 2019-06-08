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
    #print('da')
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
    profile_form.user = get_object_or_404(User, pk=request.user.pk)


    if request.method == 'POST':
        #user_form = UserForm(request.POST, instance=request.user)
        #print('da')
        
        print('user:',profile_form.user)
        print(user_form.errors, 'mda', profile_form.errors)
        if user_form.is_valid() and profile_form.is_valid():
            #profile = PersonProfile(image = request.FILES['image'])

            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            user_form.save()
 
            #return redirect('settings:profile')
            #return HttpResponse('success!')
            return redirect('/feed/')
       
    
    return render(request, 'userApp/reg.html', {
    'user_form': user_form,
    'profile_form': profile_form,
    })
    # return HttpResponse('test!')
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
            'event_request': AcceptedEvent.objects.filter(user=get_object_or_404(PersonProfile, user=self.request.user), accepted=False),
            'accepted_events': AcceptedEvent.objects.filter(user=get_object_or_404(PersonProfile, user=self.request.user), accepted=True),
            'len_events': len(AcceptedEvent.objects.filter(user=get_object_or_404(PersonProfile, user=self.request.user), accepted=False))
        })
        context.update({
             
            'selected_events': EventProfile.objects.filter(pk__in=[i.event.id for i in context['event_follows']], date=date)
        })

        return context 

def MusiciansListRequest(request):
    response_data = {}
    print(request.POST['id'])
    
    if request.method == 'POST':
        parsemus = {}
        parsegroup = {}
        for i in request.POST["select"][1:-1].split(','):
            tmp = i[1:-1]#str(i).split(':')
            print(tmp)
            if(tmp[0] == 'm'):
                p = AcceptedEvent()
                p.user = PersonProfile.objects.filter(pk=int(tmp[2:]))[0]
                p.event = EventProfile.objects.filter(pk=request.POST['id'])[0]
                p.save()
            if(tmp[0] == 'g'):
                p = AcceptedEvent()
                p.group = GroupProfile.objects.filter(pk=int(tmp[2:]))[0]
                p.event = EventProfile.objects.filter(pk=request.POST['id'])[0]
                p.save()
    response_data['da'] = 'da'
    return JsonResponse(response_data)

def EventCreate(request):
    response_data = {}
    if request.method == 'POST':
        p = EventProfile()
        p.name = request.POST["name"]
        p.address = request.POST["address"]
        p.date = request.POST["date"]
        p.description = request.POST["description"]
        p.company = get_object_or_404(PersonProfile, user=request.user)
        p.save()
        #print(p.pk)
        response_data['id'] = p.pk
        response_data['token'] = request.POST["csrfmiddlewaretoken"]
    return JsonResponse(response_data)


def EventFollowList(request):
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
    myprofile = get_object_or_404(PersonProfile, user=request.user)
    isfollow=False
    if (persondetail.followed_by.filter(user=request.user)):
        print('dada')
        isfollow=True
    else: print('netnet')
    

    acceptedGroup = AcceptedGroup.objects.filter(user=get_object_or_404(PersonProfile, user=request.user), accepted=True)
    print(acceptedGroup)
    return render(request, 'userApp/profile.html', 
    {'profile':persondetail,
    'userprofile':userdetail,
    'event_follows': Participation.objects.filter(userProfile=get_object_or_404(PersonProfile, pk=person_id)),
    'isfollow':isfollow,
    })


class GroupCreate(CreateView):
    model = GroupProfile
    template_name = 'userApp/newgroup.html'
    form_class = GroupForm
    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        #print(post)
        m = AcceptedGroup()
        m.group = post
        m.user = get_object_or_404(PersonProfile, user=self.request.user)
        m.accepted = True
        m.save()
        return redirect('/feed/')


    

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
    eventform = Event(request.POST)
    musicians = PersonProfile.objects.filter(spec=1)
    groups = GroupProfile.objects.all()
    if request.method == 'POST':
        if eventform.is_valid():
            p_profile = get_object_or_404(PersonProfile, user=request.user)
            p_profile.save()
            doc = eventform.save(commit=False)
            doc.company = p_profile
            doc.save()
            # print(redirect('/myevents/'))
            return redirect('/myevents/')
    else: 
        # return redirect('/myevents/') 
        return render(request, 'userApp/newevent.html', {'events':eventform, 'musicians': musicians, 'groups': groups})
    

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

class UserUpdate(UpdateView):
    model = PersonProfile
    # fields = ['birth_date', 'adress', 'phone', 'description','image', 'nickname','genres', 'instruments', 'soundcloud', 'company',]
    form_class=ProfileForm
    second_form_class = UserForm

    # def get_context_data(self, **kwargs):
        # context = super(UserUpdate, self).get_context_data(**kwargs)
        # print(self.form_class)
        # context.update({ 
        #     'mda': self.form_class(self.request.GET, instance=self.request.user),
        # 'user_form' : self.second_form_class(self.request.GET, instance=self.request.user),
        # })
    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return redirect('/feed/')

def follow(request, pk):
    p = get_object_or_404(PersonProfile, user=request.user)
    followman = get_object_or_404(PersonProfile, pk=pk)
    p.followers.add(followman)
    return redirect("/{}/".format(pk))

    
def RequestEventAccept(request):
    event_id = (request.POST["id"])
    user_id = get_object_or_404(PersonProfile, user=request.user)
    response_data = {}
    if request.method == 'POST':
        if request.POST["act"] == "True":
            pp = AcceptedEvent.objects.filter(user=user_id, event=event_id)
            for p in pp:
                p.accepted = True
                p.save()
            response_data["accepted"] = True
        else:
            p = AcceptedEvent.objects.filter(user=user_id, event=event_id)[0]
            p.delete()
            response_data["accepted"] = False
    response_data["parent"] =request.POST["parent"]
    return JsonResponse(response_data)

    

def unfollow(request, pk):
    p = get_object_or_404(PersonProfile, user=request.user)
    followman = get_object_or_404(PersonProfile, pk=pk)
    p.followers.remove(followman)

    return redirect("/{}/".format(pk))
  


# def UserUpdate(request,pk):
#     user_form = UserForm(request.POST, instance=request.user)
#     profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
#     profile_model = get_object_or_404(PersonProfile, user=request.user)
    
#     if request.method == 'POST':

#         if user_form.is_valid() and profile_form.is_valid():
#             #profile = PersonProfile(image = request.FILES['image'])

#             profile = profile_form.save(commit=False)
#             profile.user = request.user
#             profile.save()
#             user_form.save()

#             return redirect('/feed/')

#     return render(request, 'userApp/personprofile_form.html', {
#     'user_form': user_form,
#     'form': profile_form,
#     'profile_model': profile_model,
#     })


