from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class CustomUserChange(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']
    

class CustomUserCreation(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']