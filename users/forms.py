from django.contrib.auth.forms import UserCreationForm  
from django import forms
from django.contrib.auth.models import User 

class RegisterForm(UserCreationForm):
    username = forms.CharField(label = "Channel name")
    class Meta:
        model = User
        fields = [ "username","email", "password1", "password2"]