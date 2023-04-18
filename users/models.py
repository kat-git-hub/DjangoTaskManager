from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    user_name = models.CharField(max_length=100, verbose_name="User name")

    def __str__(self):
        return self.username

    def full_name(self):
        return self.get_full_name()
