from rest_framework import serializers
from .models import Driver, Verification


class DriverSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField('get_id')
    email = serializers.SerializerMethodField('get_email')
    is_verified = serializers.SerializerMethodField('get_verified')

    class Meta:
        model = Driver
        fields = [
            'id', 'name', 'email', 'phone_number', 'avatar', 'is_verified'
        ]

    def get_email(self, obj):
        return obj.user.email

    def get_id(self, obj):
        return obj.user.id

    def get_verified(self, obj):
        return Verification.objects.filter(user=obj).is_verified


class VerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verification
        fields = '__all__'


class DriverDetailSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField('get_id')
    email = serializers.SerializerMethodField('get_email')
    verification = serializers.SerializerMethodField('get_verification')

    class Meta:
        model = Driver
        fields = '__all__'

    def get_email(self, obj):
        return obj.user.email

    def get_id(self, obj):
        return obj.user.id

    def get_verification(self, obj):
        return VerificationSerializer(Verification.objects.filter(user=obj)).data


# class
