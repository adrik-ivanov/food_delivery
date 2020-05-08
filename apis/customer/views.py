from django.shortcuts import render
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSet, ModelViewSet
from apis.user.models import CustomUser


class CustomerPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == CustomUser.CUSTOMER
