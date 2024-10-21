from rest_framework import serializers
from .models import TwitchLiveAction, BlueskyPostReaction

class TwitchLiveActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitchLiveAction
        fields = '__all__'

class BlueskyPostReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlueskyPostReaction
        fields = '__all__'
