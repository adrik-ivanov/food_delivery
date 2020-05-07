from rest_framework import serializers
from .models import Driver


class DriverSerializer(serializers.ModelSerializer):
    mail = serializers.EmailField(max_length=None, min_length=None, allow_blank=False)

    class Meta:
        model = Driver
        fields = '__all__'


