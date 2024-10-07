from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserTokenSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserToken
        fields = ['user', 'provider', 'access_token', 'refresh_token', 'expires_at']
