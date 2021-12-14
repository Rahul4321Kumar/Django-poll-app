from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Profile(models.Model):
    """This class is used to create profile model"""
    SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
        ('U', 'Unsure',),
    )

    user = models.OneToOneField(User, on_delete= models.CASCADE)
    gender = models.CharField(max_length=1, choices=SEX_CHOICES,)
    address = models.TextField(max_length=200)
    profile_img = models.ImageField(default = 'media/default.jpg',
                                    upload_to = 'media',
                                    null = True, blank = True,
                                    )

    def __str__(self):
        return f"{self.user.username}'s profile"

    def get_absolute_url(self):
        return reverse("accounts:edit_profile")
 