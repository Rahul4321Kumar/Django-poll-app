from django.urls import path

from accounts.views import (
    Login,SignUpView, LogoutView
)

app_name = 'accounts'
urlpatterns = [
    path('register', SignUpView.as_view(), name='register'),
    path('login', Login.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    
]