from django import forms
from .models import *

class EventForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['caption', 'image']