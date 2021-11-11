from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'accounts/dashboard.html')

def user(request):
    return render(request, 'accounts/user.html')

def picture(request):
    return render(request, 'accounts/pictures.html')
