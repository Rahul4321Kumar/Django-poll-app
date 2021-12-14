from django.contrib.auth.models import User
from django import forms
from accounts.tasks import send_confirmation_mail_task
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from accounts.models import Profile


class UserRegistrationForm(UserCreationForm):
    """This class is used to create a new user registration form"""
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    
   
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

    
    def clean_email(self):
        self.email = self.cleaned_data['email']
        return self.email.lower()

    def clean_username(self):
        
        username = self.cleaned_data['username']
        send_confirmation_mail_task.delay(
            username,self.email,
        )
        return username.lower()
        
class UserLoginForm(AuthenticationForm):
    """This class is used to create a new login form"""
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                                'placeholder':'Username',
                                'required': True, 'autofocus' : True}),
                                )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',
                                'placeholder':'Password',
                                'required': True}),
                                )


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
