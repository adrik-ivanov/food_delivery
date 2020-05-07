from rest_framework import serializers
from .models import CustomUser
from apis.customer.models import Customer
from apis.driver.models import Driver


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        if user.role == CustomUser.CUSTOMER:
            Customer.objects.create(user=user)
        if user.role == CustomUser.DRIVER:
            Driver.objects.create(user=user)
        return user


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=None, min_length=None, allow_blank=False)
    password = serializers.CharField(style={'input_type': 'password'})


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=None, min_length=None, allow_blank=False)
    password = serializers.CharField(style={'input_type': 'password'})
    name = serializers.CharField(max_length=256, allow_null=False)


