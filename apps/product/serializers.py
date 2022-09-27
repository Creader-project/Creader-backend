# _*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '28/06/2021 17:38'

from .models import Top_up_item, Subscription_Plan, User_profile
from user.models import AuthUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for users.
    """
    class Meta:
        model = AuthUser
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email"
        )


class TopUpItemSerializer(serializers.ModelSerializer):
    """
    Serializer for top up items.
    """
    class Meta:
        model = Top_up_item
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    """
    Serializer for subscriptions.
    """
    class Meta:
        model = Subscription_Plan
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for user profile.
    """
    user = UserSerializer(read_only=True)
    plan = SubscriptionSerializer(read_only=True)

    class Meta:
        model = User_profile
        fields = "__all__"
