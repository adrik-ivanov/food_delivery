from rest_framework import serializers
from .models import CustomUser


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class DriverSerializer(serializers.ModelSerializer):
    mail = serializers.EmailField(max_length=None, min_length=None, allow_blank=False)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=None, min_length=None, allow_blank=False)
    password = serializers.CharField(style={'input_type': 'password'})


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=None, min_length=None, allow_blank=False)
    password = serializers.CharField(style={'input_type': 'password'})
    name = serializers.CharField(max_length=256, allow_null=False)


