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
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.db.models import *
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
    #TEMP
  

# @login_required
def feed(request):
    persons = PersonProfile.objects


    return render(request, 'userApp/feed.html', {'persons':persons})

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

            

        return result

    # def get_queryset(self):
        
    #     if self.request.GET.get('query') !=None:
    #         query=self.request.GET.get('query')
    #         return HttpResponse(query)
    #         return PersonProfile.objects.filter(Q(nickname=query))
    #     else:
    #         return PersonProfile.objects.all()
            

# def allpersons(request):
#     persons = PersonProfile.objects
#     return render(request, 'userApp/allpersons.html', {'persons':persons})
 
def profile(request, person_id):
    persondetail = get_object_or_404(PersonProfile, pk=person_id)
    #persondetail.email=''
    userdetail = persondetail.user
    acceptedGroup = AcceptedGroup.objects.filter(user=get_object_or_404(PersonProfile, user=request.user), accepted=True)
    print(acceptedGroup)
    return render(request, 'userApp/profile.html', 
    {'profile':persondetail,
    'userprofile':userdetail,
    })




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