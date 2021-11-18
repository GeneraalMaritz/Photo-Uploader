from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('user/<str:pk>/', views.user, name="user"),
    path('picture/', views.picture, name="pictures"),
    path('create_upload/', views.createUpload, name="create_upload"),
    path('update_upload/<str:pk>/', views.updateUpload, name="update_upload")
]
