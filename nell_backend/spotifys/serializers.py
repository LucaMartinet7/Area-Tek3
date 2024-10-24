from rest_framework import serializers
from .models import SpotifyAction

class SpotifyActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyAction
        fields = '__all__'
