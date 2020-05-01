from django.db import models
from phone_field import PhoneField

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=256, null=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')

    def __str__(self):
        return self.name


# class CustomerDetail(models.Model):
