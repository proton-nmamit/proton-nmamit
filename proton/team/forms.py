from django import forms
from team.models import member

class memberForm(forms.ModelForm):
    class Meta:
        model = member
        exclude = ['user', 'position']  # Exclude the user field from the form