from django.forms import ModelForm
from .models import *

class UploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = '__all__'
