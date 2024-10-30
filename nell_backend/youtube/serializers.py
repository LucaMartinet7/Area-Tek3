from rest_framework import serializers
from .models import YouTubeAction, SpotifyPlaylistReaction

class YouTubeActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTubeAction
        fields = '__all__'

class SpotifyPlaylistReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyPlaylistReaction
        fields = '__all__'
