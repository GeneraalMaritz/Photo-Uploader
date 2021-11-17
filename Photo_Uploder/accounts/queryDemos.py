from .models import *

users = User.objects.all()

userFirst = User.objects.first()

userFirst.upload_set.all()



