from django import forms


class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=15,label_suffix=' :')
    last_name = forms.CharField( max_length=15,label_suffix=' :')
    username = forms.CharField( max_length=150,label_suffix=' :')
    email = forms.EmailField( max_length=20,label_suffix=' :')
    password = forms.CharField(max_length=32, widget=forms.PasswordInput,label_suffix=' :')

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
