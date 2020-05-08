from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSet, ModelViewSet
from rest_framework.permissions import BasePermission, IsAuthenticated
from .serializers import CategorySerializer, RestaurantSerializer
from .models import Category, Restaurant

# Create your views here.
from apis.customer.views import CustomerPermission


class CategoryViewSet(ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated, CustomerPermission)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class RestaurantViewSet(ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated, CustomerPermission)
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()