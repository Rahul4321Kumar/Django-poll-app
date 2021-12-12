from django.urls import path

from accounts.views import (
    register, login, logout,
    CreateProfile, edit_profile,
)

app_name = 'accounts'
urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('create_profile', CreateProfile.as_view(), name='create_profile'),
    path('edit_profile', edit_profile, name='edit_profile'),
]