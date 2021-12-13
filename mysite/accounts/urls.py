from django.urls import path
from django.contrib.auth.decorators import login_required
from accounts.views import (
    Login,
    CreateProfile, EditProfileForm,
    SignUpView, LogoutView
)

app_name = 'accounts'
urlpatterns = [
    path('register', SignUpView.as_view(), name='register'),
    path('login', Login.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('create_profile', login_required(CreateProfile.as_view()),
    name='create_profile'),
    path('edit_profile', login_required(EditProfileForm.as_view()),
    name='edit_profile'),
]