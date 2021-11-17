from django.contrib import admin
from django.urls import path
from . import views





urlpatterns = [
    path('', views.home),
    path('user/<str:pk>/', views.user),
    path('picture/', views.picture),

]