import uuid

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(null=True, max_length=256)
    role = models.SmallIntegerField(blank=False, default=CUSTOMER)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']

    objects = CustomUserManager()

    def get_full_name(self):
        return self.username

    def __str__(self):
        return self.email

    def get_role_name(self):
        return self.ROLE_CHOICES[self.role]
