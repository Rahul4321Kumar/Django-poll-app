from django.urls import path
from django.contrib.auth.decorators import login_required
from accounts.views import (
    Login,RegisterForm,main,logout,
    activate,
)

app_name = 'accounts'
urlpatterns = [
    path('register', RegisterForm.as_view(), name='register'),
    path('login',Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('main', main, name='main'),
    path('activate/<uidb64>/<token>',
         activate, name='activate'),
]