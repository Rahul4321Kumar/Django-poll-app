from django.contrib.auth.models import User
from django import forms

from accounts.models import Profile


class UserRegistrationForm(forms.Form):
    """This class is used to create a new user registration form"""
    first_name = forms.CharField(max_length=15, label_suffix=' :')
    last_name = forms.CharField(max_length=15, label_suffix=' :')
    username = forms.CharField(max_length=150, label_suffix=' :')
    email = forms.EmailField(max_length=20, label_suffix=' :')
    password = forms.CharField(max_length=32, widget=forms.PasswordInput, label_suffix=' :')
    confirm_password = forms.CharField(max_length=32, label='Confirm_Password', widget=forms.PasswordInput, label_suffix=' :')


class UserLoginForm(forms.Form):
    """This class is used to create a new login form"""
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    """This class is used to create a new user Profile"""
    class Meta:
        model = Profile
        fields = ['gender', 'address', 'profile_img']
   

class UserUpdateForm(forms.ModelForm):
    """This class is used to update user model"""
    class Meta:
        """This class takes model and feild attribute to change"""
        model = User
        fields = ['first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    """This class is used to update profile model"""
    class Meta:
        """This class takes model and feild attribute to change"""
        model = Profile
        fields = ['gender', 'address', 'profile_img']
