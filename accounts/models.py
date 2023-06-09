from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from accounts.managers import UserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    email = models.EmailField(("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

