from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic import CreateView, RedirectView, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout


from accounts.models import Profile
from accounts.forms import (
    UserRegistrationForm, UserLoginForm, ProfileForm, UserUpdateForm,
    ProfileUpdateForm,UserRegistrationForm
)


class CreateProfile(CreateView):
    """
    This class based view is used to create a new profile
    """
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile.html'

    def form_valid(self, form):
        """
        This function used to check if the form is valid save data in databases
        """
        form.instance.user = self.request.user
        print(form.instance.user, self.request.user)
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        """
        This function checks whether the profile exits or not
        """
        if Profile.objects.filter(user=self.request.user).exists():
            messages.info(request, 'Profile already exists')
            return redirect(reverse('accounts:edit_profile'))
        return super().get(request, *args, **kwargs)


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

    
class EditProfileForm(TemplateView):
    user_form = UserUpdateForm
    profile_form = ProfileUpdateForm
    template_name = 'accounts/show_profile.html'

    def post(self,request):
        """
        This function is responsible to update data in user and profile table
        """
        post_data =request.POST or None
        file_data = request.FILES or None

        user_form = UserUpdateForm(post_data, instance=request.user)
        profile_form = ProfileUpdateForm(post_data, file_data,
                                        instance=request.user.profile
                                        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.info(request, 'Profile updated successfully')
            return redirect(reverse('accounts:edit_profile'))

        context = self.get_context_data(
                                        user_form = user_form,
                                        profile_form = profile_form
                                    )

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)