from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.Form):
    """This class is used to create a new user registration form"""
    first_name = forms.CharField(max_length=15, label_suffix=' :')
    last_name = forms.CharField(max_length=15, label_suffix=' :')
    username = forms.CharField(max_length=150, label_suffix=' :')
    email = forms.EmailField(max_length=80, label_suffix=' :')
    password = forms.CharField(max_length=32, widget=forms.PasswordInput, label_suffix=' :')
    confirm_password = forms.CharField(max_length=32, label='Confirm_Password', widget=forms.PasswordInput, label_suffix=' :')
        

class UserLoginForm(forms.Form):
    """This class is used to create a new login form"""
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)