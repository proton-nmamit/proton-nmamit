# Import necessary modules from Django
from django import forms
from .models import *  # Import all models from the current app
from django.contrib.auth.models import User  # Import the built-in User model
from django.contrib.auth.forms import UserCreationForm  # Import the UserCreationForm

# Define a custom UserRegistrationForm that inherits from UserCreationForm
class UserRegistrationForm(UserCreationForm):
    # Add an email field to the form
    email = forms.EmailField()

    # Define the Meta class to specify the model and fields for the form
    class Meta:
        # Specify the model for the form (in this case, the built-in User model)
        model = User
        # Specify the fields to include in the form
        fields = ('username', 'email', 'password1', 'password2')