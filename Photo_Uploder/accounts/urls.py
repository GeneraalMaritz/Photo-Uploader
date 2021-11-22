from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('user/<str:pk>/', views.user, name="user"),
    path('picture/', views.picture, name="pictures"),
    path('create_upload/<str:pk>/', views.createUpload, name="create_upload"),
    path('update_upload/<str:pk>/', views.updateUpload, name="update_upload"),
    path('delete_upload/<str:pk>/', views.deleteUpload, name="delete_upload"),
    path('add_picture/', views.addPicture, name="add_picture"),
    path('view_picture/<str:pk>', views.viewPicture, name="view_picture"),
    path('gallery', views.gallery, name="gallery")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
