from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class User(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Picture(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    picture = models.ImageField(null=False, blank=False, default="Image")
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(default="Description")
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Upload(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    picture = models.ForeignKey(Picture, null=True, on_delete=models.SET_NULL)
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)





