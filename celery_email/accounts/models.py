from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    This class used to create a new custom user
    """
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.email