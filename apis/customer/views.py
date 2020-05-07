from django.shortcuts import render
from rest_framework.permissions import BasePermission

from apis.user.models import CustomUser


class CustomerPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == CustomUser.CUSTOMER


