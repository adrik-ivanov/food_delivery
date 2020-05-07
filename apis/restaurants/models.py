import uuid
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from apis.customer.models import Customer
from apis.customer.models import Address
from apis.driver.models import Driver


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256, default='')
    image = models.URLField(max_length=1024, default='')

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256, default='')
    photo = models.URLField(max_length=1024, default='')
    phone_number = PhoneNumberField(blank=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=15, null=False, default=0.0)
    longitude = models.DecimalField(max_digits=20, decimal_places=15, null=False, default=0.0)
    formatted_address = models.CharField(max_length=1024, default='', blank=True, )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256, default='')
    thumbnail = models.URLField(max_length=1024, default='')
    banner = models.URLField(max_length=1024, default='')
    price = models.FloatField()
    currency = models.CharField(max_length=8, default='usd')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    score = models.FloatField()
    description = models.CharField(max_length=1024, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
