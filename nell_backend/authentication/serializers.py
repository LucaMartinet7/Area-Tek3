from django.contrib.auth.models import User
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer as DefaultRegisterSerializer

class CustomRestAuthRegisterSerializer(DefaultRegisterSerializer):
    class Meta:
        model = User  # Specify the model
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        ref_name = 'RestAuthRegisterSerializer'  # Unique name for Swagger

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        ref_name = 'CustomRegisterSerializer'

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()  # Save the user to the database
        return user
