from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import get_user_model
from accounts.tasks import send_confirmation_mail_task
from django.utils.http import urlsafe_base64_decode
from accounts.token_generator import account_activation_token
from django.utils.encoding import force_text

from accounts.forms import (
    UserRegistrationForm, UserLoginForm,
)

User = get_user_model()

def register(request):
    """This function handle register request"""
    if request.method == 'POST':
        
        user_detail = UserRegistrationForm(request.POST)
        if user_detail.is_valid():
            first_name = user_detail.cleaned_data['first_name']
            last_name = user_detail.cleaned_data['last_name']
            username = user_detail.cleaned_data['username']
            email = user_detail.cleaned_data['email']
            password = user_detail.cleaned_data['password']
            confirm_password = user_detail.cleaned_data['confirm_password']
            
            if password == confirm_password:
                if User.objects.filter(email=email).exists():
                    messages.info(request, 'Email already exists')
                else:
                    user = User.objects.create_user(
                                                    email=email,
                                                    first_name=first_name,
                                                    last_name=last_name,
                                                    username=username,
                                                    password=password,
                                                    )
                    user.set_password(password)
                    # import pdb;pdb.set_trace()
                    send_confirmation_mail_task.delay(username,email)
                    user.save()
                    messages.success(request, 'User created successfully')
                    return redirect(reverse('accounts:login'))
            else:
                messages.info(request, 'Password not matched')
                return redirect(reverse('accounts:register'))
    else:
        user_detail=UserRegistrationForm()
        
    return render(request, 'accounts/register.html', {'form': user_detail})


def login(request):
    """This function is used to handle login request"""
    if request.method == 'POST':
        context = {'data': request.POST}
        login_detail = UserLoginForm(request.POST)
        if login_detail.is_valid():
            username = login_detail.cleaned_data['username']
            password = login_detail.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user and not user.is_email_verified:
                messages.info(request, 'Email is not verified, please check your email inbox')
                return render(request, 'accounts/login.html', context, status=401)
            if user is not None:
                auth.login(request,user)
                return render(request, 'pages/index.html')
            else:
                messages.info(request,'invalid credentials')
                return redirect(reverse('accounts:login'))
    else:
        login_detail=UserLoginForm()
    return render(request, 'accounts/login.html', {'form':login_detail})

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