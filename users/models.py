from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    def full_name(self):
        return self.get_full_name()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
