from django.db import models
from django.contrib.auth.models import AbstractUser

class LershaUser(AbstractUser):
    admin = models.BooleanField(default=False)
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def has_profile(self):
        return hasattr(self, 'profile')
