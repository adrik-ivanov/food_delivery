from rest_framework import serializers
from .models import Customer, Address, PaymentHistory, PaymentMethod


class CustomerSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField('get_id')
    email = serializers.SerializerMethodField('get_email')

    class Meta:
        model = Customer
        fields = [
            'id', 'name', 'email', 'phone_number'
        ]

    def get_email(self, obj):
        return obj.user.email

    def get_id(self, obj):
        return obj.user.id


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class CustomerDetailSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField('get_id')
    email = serializers.SerializerMethodField('get_email')
    addresses = serializers.SerializerMethodField('get_addresses')

    class Meta:
        model = Customer
        fields = '__all__'

    def get_id(self, obj):
        return obj.user.id

    def get_email(self, obj):
        return obj.user.email

    def get_addresses(self, obj):
        return AddressSerializer(Address.objects.filter(user=obj.user), many=True).data


class PaymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentHistory
        fields = '__all__'


class PaymentMethodSerializer(serializers.ModelSerializer):
    histories = serializers.SerializerMethodField('get_history')

    class Meta:
        model = PaymentMethod
        fields = '__all__'

    def get_history(self, data):
        return PaymentHistorySerializer(PaymentHistory.objects.filter(method=data), many=True).data


