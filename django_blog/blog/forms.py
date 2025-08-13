from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True) # custom field for email

    class Meta:
        model = User # specify the model to use
        fields = ['username', 'email', 'password1', 'password2'] # specify the fields to include
        #in the form , and adding custom email field

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']      # specify the fields to include in
        #the form  

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your comment here...'
            }),
        }
        labels = {
            'content': 'Your Comment'
        }        
