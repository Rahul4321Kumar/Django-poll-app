from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class MyUser(AbstractUser):
    SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
        ('U', 'Unsure',),
    )
    gender = models.CharField(verbose_name=_('Gender'), max_length=1, choices=SEX_CHOICES,)
    address = models.TextField(verbose_name=_('Address'), max_length=200)
    profile_img = models.ImageField(verbose_name=_('Profile Image'),default = 'media/default.jpg',
                                    upload_to = 'media',
                                    null = True, blank = True,
                                    )

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return f"{self.username}:{self.first_name}{self.last_name}"


