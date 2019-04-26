from django.shortcuts import render, redirect
from django import forms
# Create your views here.

def index(request):
    return redirect('login/')
    #return render(request, 'registration/login.html')

def registration(request):

    print(request.POST.get('first_name'))
    return render(request, 'mainApp/reg.html')
    

def login(request):

    return render(request, 'mainApp/login.html')
