from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserToken
from dj_rest_auth.registration.serializers import RegisterSerializer as DefaultRegisterSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserTokenSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = UserToken
        fields = ['user', 'provider', 'access_token', 'refresh_token', 'expires_at']

class CustomRestAuthRegisterSerializer(DefaultRegisterSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        ref_name = 'CustomRestAuthRegisterSerializer'  # Unique name to prevent conflicts

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        ref_name = 'CustomRegisterSerializer'  # Unique name to prevent conflicts

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()  # Save the user to the database
        return user
