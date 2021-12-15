# from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from accounts.tasks import send_confirmation_mail_task
from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, label_suffix=' :')
    email = forms.EmailField(max_length=80, label_suffix=' :')
    
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

    def send_email(self):
        send_confirmation_mail_task.delay(
            self.cleaned_data['username'], self.cleaned_data['email']
        )
        
    def save(self, commit=True):
        main_user = super().save(commit)
        self.send_email()
        return main_user

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
