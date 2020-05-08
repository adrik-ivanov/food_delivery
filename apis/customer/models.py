import uuid

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
from apis.user.models import CustomUser


class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, null=True)
    phone_number = PhoneNumberField(blank=True, help_text='Contact phone number')
    fcm_token = models.CharField(max_length=256, default='')

    def __str__(self):
        return self.name


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=20, decimal_places=15, null=False, default=0.0)
    longitude = models.DecimalField(max_digits=20, decimal_places=15, null=False, default=0.0)
    formatted_address = models.CharField(max_length=1024, default='', blank=True,)


class PaymentMethod(models.Model):
    card_number = models.CharField(max_length=64, default='')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    card_token = models.CharField(max_length=256, default='')


class PaymentHistory(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    is_error = models.BooleanField(default=False)
    description = models.CharField(max_length=256, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
