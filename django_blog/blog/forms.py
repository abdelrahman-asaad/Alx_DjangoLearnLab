from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True) # custom field for email

    class Meta:
        model = User # specify the model to use
        fields = ['username', 'email', 'password1', 'password2'] # specify the fields to include
        #in the form , and adding custom email field
