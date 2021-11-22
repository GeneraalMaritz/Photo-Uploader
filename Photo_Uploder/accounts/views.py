from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import UploadForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    uploads = Upload.objects.all()
    users = User.objects.all()

    total_users = users.count()

    total_uploads = uploads.count()

    context = {'uploads': uploads, 'users': users,
               'total_users': total_users, 'total_uploads': total_uploads}
    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
def user(request, pk):
    users = User.objects.get(id=pk)

    uploads = users.upload_set.all()
    upload_count = uploads.count()

    context = {'user': users, 'uploads': uploads, 'upload_count': upload_count}
    return render(request, 'accounts/user.html', context)


@login_required(login_url='login')
def picture(request):
    pictures = Picture.objects.all()
    return render(request, 'accounts/pictures.html', {'pictures': pictures})


@login_required(login_url='login')
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


@login_required(login_url='login')
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


@login_required(login_url='login')
def deleteUpload(request, pk):
    upload = Upload.objects.get(id=pk)

    if request.method == "POST":
        upload.delete()
        return redirect('/')
    context = {'item': upload}
    return render(request, 'accounts/delete.html', context)


@login_required(login_url='login')
def addPicture(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        photo = Picture.objects.create(
            category=category,
            description=data['description'],
            picture=image,
        )

        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'accounts/add_picture.html', context)


@login_required(login_url='login')
def viewPicture(request, pk):
    picture = Picture.objects.get(id=pk)
    return render(request, 'accounts/view_picture.html', {'picture': picture})


@login_required(login_url='login')
def gallery(request):
    category = request.GET.get('category')
    if category == None:
        pictures = Picture.objects.all()
    else:
        pictures = Picture.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {'categories': categories, 'pictures': pictures}
    return render(request, 'accounts/gallery.html', context)
