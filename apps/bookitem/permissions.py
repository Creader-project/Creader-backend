# _*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '27/07/2021 18:34'

from rest_framework import permissions
from product.models import User_profile


class IsAuthorPermission(permissions.BasePermission):
    """
    This class is used to check if the user is the author of the book
    """
    def has_permission(self, request, view):
        return bool(request.user.role == 2)
