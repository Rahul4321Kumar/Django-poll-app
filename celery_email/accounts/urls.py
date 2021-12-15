from django.urls import path
from django.contrib.auth.decorators import login_required
from accounts.views import (
    login,register,main,logout,
    activate,
)

app_name = 'accounts'
urlpatterns = [
    path('register', register, name='register'),
    path('login',login, name='login'),
    path('logout', logout, name='logout'),
    path('main', main, name='main'),
    path('activate/<uidb64>/<token>',
         activate, name='activate'),
]