from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Picture(models.Model):
    name = models.CharField(max_length=200, null=True)
    size = models.IntegerField(null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Upload(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    picture = models.ForeignKey(Picture, null=True, on_delete=models.SET_NULL)
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.user) + " Upload"
