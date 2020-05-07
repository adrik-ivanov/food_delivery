from django.shortcuts import render
from rest_framework.permissions import BasePermission
# Create your views here.
from apis.user.models import CustomUser


class DriverPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == CustomUser.DRIVER


