from django.shortcuts import render, redirect
from django import forms
# Create your views here.

def index(request):
    return redirect('login/')
    #return render(request, 'registration/login.html')


