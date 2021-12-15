from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from accounts.token_generator import account_activation_token
from django.utils.encoding import force_text
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login

from accounts.forms import (
    RegisterForm, UserLoginForm,
)

User = get_user_model()

class RegisterForm(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    model = User
    
    def get_success_url(self):
        return reverse('accounts:login')
    
class Login(LoginView):
    """
    Provides users the ability to login
    """
    authentication_form = UserLoginForm
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        print(form.get_user().is_email_verified)
        if form.get_user() and not form.get_user().is_email_verified:
            messages.info(self.request, 'Email is not verified, please check your email inbox')
            return render(self.request, 'accounts/login.html')
        login(self.request, form.get_user())
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accounts:main')

def logout(request):
    """This function is used to handle logout request"""
    auth.logout(request)
    return redirect(reverse('accounts:main'))

def main(request):
    return render(request, 'accounts/main.html')


def activate(request, uidb64, token):

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))

        user = User.objects.get(pk=uid)
        print(user)

    except Exception:
        user = None

    if user and account_activation_token.check_token(user, token):
        user.is_email_verified = True
        user.save()

        messages.add_message(request, messages.SUCCESS,
                             'Email verified, you can now login')
        return redirect(reverse('accounts:login'))

    return render(request, 'accounts/activate-failed.html', {"user": user})