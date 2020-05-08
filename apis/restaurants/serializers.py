from rest_framework import serializers
from .models import Restaurant, Category, Food, Feedback, Order
from ..customer.serializers import AddressSerializer, CustomerSerializer
from ..driver.serializers import DriverSerializer


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('get_user')
    food = serializers.SerializerMethodField('get_food')

    class Meta:
        model = Feedback
        fields = '__all__'

    def get_user(self, obj):
        return CustomerSerializer(obj.user).data

    def get_food(self, obj):
        return FoodSerializer(obj.food).data

class OrderSerializer(serializers.ModelSerializer):
    food = serializers.SerializerMethodField('get_food')
    address = serializers.SerializerMethodField('get_address')
    customer = serializers.SerializerMethodField('get_customer')
    driver = serializers.SerializerMethodField('get_driver')

    class Meta:
        model = Order
        fields = '__all__'

    def get_food(self, obj):
        return FoodSerializer(obj.food).data

    def get_address(self, obj):
        return AddressSerializer(obj.address).data

    def get_customer(self, obj):
        return CustomerSerializer(obj.customer).data

    def get_driver(self, obj):
        return DriverSerializer(obj.driver).data
