from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic import CreateView, RedirectView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout


from accounts.forms import (
    UserRegistrationForm, UserLoginForm,
    UserRegistrationForm,
)





class SignUpView(CreateView):
    """
    Provides users the ability to register
    """
    model = User
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    
    def get_success_url(self):
        return reverse('accounts:login')

    def form_valid(self, form):
        print(form)
        return super().form_valid(form)

    
class Login(LoginView):
    """
    Provides users the ability to login
    """
    authentication_form = UserLoginForm
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('polls:index')


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

    
