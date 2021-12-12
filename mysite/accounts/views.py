from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

from accounts.models import Profile
from accounts.forms import (
    UserRegistrationForm, UserLoginForm, ProfileForm, UserUpdateForm,
    ProfileUpdateForm,
)


class CreateProfile(CreateView):
    """This class based view is used to create a new profile"""
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile.html'

    def form_valid(self, form):
        """This function used to check if the form is valid save data in databases"""
        form.instance.user = self.request.user
        print(form.instance.user, self.request.user)
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        """This function checks whether the profile exits or not"""
        if Profile.objects.filter(user=self.request.user).exists():
            messages.info(request, 'Profile already exists')
            return redirect(reverse('accounts:edit_profile'))
        return super().get(request, *args, **kwargs)


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
                    user.save()
                    messages.success(request, 'User created successfully')
                    return redirect(reverse('accounts:login'))
            else:
                messages.info(request, 'Password not matched')
                return redirect(reverse('accounts:register'))
    else:
        user_detail = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': user_detail})


def login(request):
    """This function is used to handle login request"""
    if request.method == 'POST':
        login_detail = UserLoginForm(request.POST)
        if login_detail.is_valid():
            username = login_detail.cleaned_data['username']
            password = login_detail.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return render(request, 'pages/index.html')
            else:
                messages.info(request, 'invalid credentials')
                return redirect(reverse('accounts:login'))
    else:
        login_detail = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': login_detail})


def logout(request):
    """This function is used to handle logout request"""
    auth.logout(request)
    return redirect(reverse('polls:main'))


@login_required
def edit_profile(request):
    """This function is used to handle profile update request"""
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES,
                                        instance=request.user.profile
                                        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.info(request, 'Profile updated successfully')
            return redirect(reverse('accounts:edit_profile'))
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form' : user_form,
        'profile_form' : profile_form
    }
    return render(request, 'accounts/show_profile.html', context)
