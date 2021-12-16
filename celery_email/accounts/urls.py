from django.urls import path
from django.contrib.auth.decorators import login_required
from accounts.views import (
    Login,RegisterForm,MainView,LogoutView,
    activate,
)

app_name = 'accounts'
urlpatterns = [
    path('register', RegisterForm.as_view(), name='register'),
    path('login',Login.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('main', MainView.as_view(), name='main'),
    path('activate/<uidb64>/<token>',
         activate, name='activate'),
]