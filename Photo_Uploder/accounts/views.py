from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import UploadForm


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
    upload_count = uploads.count()

    context = {'user': users, 'uploads': uploads, 'upload_count': upload_count}
    return render(request, 'accounts/user.html', context)


def picture(request):
    pictures = Picture.objects.all()
    return render(request, 'accounts/pictures.html', {'pictures': pictures})


def createUpload(request, pk):
    users = User.objects.get(id=pk)
    form = UploadForm()
    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, 'users': users}
    return render(request, 'accounts/upload_form.html', context)


def updateUpload(request, pk):
    upload = Upload.objects.get(id=pk)
    form = UploadForm(instance=upload)

    if request.method == 'POST':
        form = UploadForm(request.POST, instance=upload)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/upload_form.html', context)


def deleteUpload(request, pk):
    upload = Upload.objects.get(id=pk)

    if request.method == "POST":
        upload.delete()
        return redirect('/')
    context = {'item': upload}
    return render(request, 'accounts/delete.html', context)


def addPicture(request):
    return render(request, 'accounts/add_picture.html')


def viewPicture(request, pk):
    return render(request, 'accounts/view_picture.html')


def gallery(request):
    return render(request, 'accounts/gallery.html')
