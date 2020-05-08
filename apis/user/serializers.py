from rest_framework import serializers
from .models import CustomUser
from apis.customer.models import Customer
from apis.driver.models import Driver
from ..customer.serializers import CustomerSerializer
from ..driver.serializers import DriverSerializer


class UserSerializer(serializers.ModelSerializer):
    detail = serializers.SerializerMethodField('get_detail')

    class Meta:
        model = CustomUser
        fields = '__all__'

    def get_detail(self, obj):
        if obj.role == CustomUser.CUSTOMER:
            return CustomerSerializer(Customer.objects.filter(user__id=obj.id)).data
        if obj.role == CustomUser.DRIVER:
            return DriverSerializer(Driver.objects.filter(user__id=obj.id)).data
        return None


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=None, min_length=None, allow_blank=False)
    password = serializers.CharField(style={'input_type': 'password'})


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=None, min_length=None, allow_blank=False)
    password = serializers.CharField(style={'input_type': 'password'})
    name = serializers.CharField(max_length=256, allow_null=False)

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        if user.role == CustomUser.CUSTOMER:
            Customer.objects.create(user=user)
        if user.role == CustomUser.DRIVER:
            Driver.objects.create(user=user)
        return user

