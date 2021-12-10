from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse

from accounts.forms import UserRegistrationForm,UserLoginForm


def register(request):
    if request.method == 'POST':
        user_detail=UserRegistrationForm(request.POST)
        if user_detail.is_valid():
            first_name = user_detail.cleaned_data['first_name']
            last_name = user_detail.cleaned_data['last_name']
            Username = user_detail.cleaned_data['username']
            Email = user_detail.cleaned_data['email']
            Password = user_detail.cleaned_data['password']
            confirm=make_password(Password)
            print(confirm)
            user=User.objects.create_user(email=Email,first_name=first_name,last_name=last_name,username=Username,password=confirm)
            user.save()
            messages.success(request, 'User created successfully')
            return redirect(reverse('polls:main'))
    else:
        user_detail=UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': user_detail})


def login(request):
    if request.method == 'POST':
        login_detail = UserLoginForm(request.POST)
        if login_detail.is_valid():
            username = login_detail.cleaned_data['username']
            password = login_detail.cleaned_data['password']
            user=auth.authenticate(username=username,password=password)
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
  auth.logout(request)
  return redirect(reverse('polls:main'))