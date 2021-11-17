from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    uploads = Upload.objects.all()
    users = User.objects.all()

    total_users = users.count()

    total_uploads = uploads.count()

    context = {'uploads': uploads, 'users': users,
               'total_users': total_users, 'total_uploads': total_uploads}
    return render(request, 'accounts/dashboard.html', context)


def user(request, pk):
    users = User.objects.get(id=pk)

    uploads = users.upload_set.all()

    context = {'user': users, 'uploads': uploads}
    return render(request, 'accounts/user.html')


def picture(request):
    pictures = Picture.objects.all()
    return render(request, 'accounts/pictures.html', {'pictures': pictures})
