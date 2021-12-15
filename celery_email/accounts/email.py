from django.template import Context
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from accounts.token_generator import account_activation_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model

User = get_user_model()


def send_confirmation_mail(username, email):
  
    try:
        user = User.objects.get(email=email)
        
        current_site = Site.objects.get_current().name
        print(current_site)
        message = {
            'username': username,
            'email': email,
            'domain': current_site,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        }
        email_subject = 'Activation Mail'
        email_body = render_to_string('accounts/activation_mail.html', message)

        email = EmailMessage(
            subject=email_subject, body=email_body, 
            from_email=settings.EMAIL_HOST_USER, to=[user.email],
        )
        return email.send(fail_silently=False)
    except Exception as e:
        return ("Multiple user Found with  this email or no user found")