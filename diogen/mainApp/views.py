from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mainApp/start_page.html')

def register(request):
    return render(request, 'mainApp/reg.html')