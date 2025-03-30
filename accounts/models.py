from django.db import models
from django.contrib.auth.models import AbstractUser


from accounts.manager import UserManager


class User(AbstractUser):

    email = models.EmailField(unique=True)
    username = models.CharField(null=True, blank=True, max_length=30)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    def __str__(self):
        return self.email


class SetToken(models.Model):
    """
    token is unique
    """

    token = models.CharField(max_length=80, unique=True)
    email = models.EmailField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Token Id {self.token}"


class BlackListEmail(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.id} {self.email}"
