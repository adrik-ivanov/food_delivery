import time
from datetime import datetime, timedelta

import jwt
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


from food_delivery import settings
from .managers import CustomUserManager


class Role(models.Model):
    DRIVER = 1
    CUSTOMER = 2
    RESTAURANT = 3
    ADMIN = 4
    ROLE_CHOICES = (
        (DRIVER, 'driver'),
        (CUSTOMER, 'customer'),
        (RESTAURANT, 'restaurant'),
        (ADMIN, 'admin')
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(null=True, max_length=256)
    role = models.ManyToManyField(Role, blank=False, default=Role.CUSTOMER)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']

    objects = CustomUserManager()

    def get_full_name(self):
        return self.username

    def __str__(self):
        return self.email
