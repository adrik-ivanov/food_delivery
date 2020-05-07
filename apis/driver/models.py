import uuid
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

# Create your models here.
from django.utils import timezone

from apis.user.models import CustomUser


class Driver(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, null=True)
    avatar = models.URLField(max_length=1024, null=False, default='')
    birthday = models.DateField(default=timezone.now, null=False)
    phone_number = PhoneNumberField(blank=True)
    account_balance = models.FloatField(default=0.0)
    total_income = models.FloatField(default=0.0)
    fcm_token = models.CharField(max_length=256, default='')

    def __str__(self):
        return self.name


class Verification(models.Model):

    user = models.ForeignKey(Driver, on_delete=models.CASCADE)
    id_card = models.URLField(max_length=1024, default='')
    driver_license = models.URLField(max_length=1024, default='')
    vehicle_license = models.URLField(max_length=1024, default='')
    is_verified = models.BooleanField(default=False)
    description = models.CharField(max_length=1024, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)