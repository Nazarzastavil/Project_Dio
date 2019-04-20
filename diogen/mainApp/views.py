from django.shortcuts import render
from django import forms
# Create your views here.

def index(request):
    return render(request, 'mainApp/start_page.html')

def registration(request):

    print(request.POST.get('first_name'))
    return render(request, 'mainApp/reg.html')
    
