from rest_framework import serializers
from .models import YouTubeWatchAction, GoogleCalendarEventReaction, GoogleCalendarCreateAction, YouTubeVideoReaction

class YouTubeWatchActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTubeWatchAction
        fields = '__all__'


class GoogleCalendarEventReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleCalendarEventReaction
        fields = '__all__'


class GoogleCalendarCreateActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleCalendarCreateAction
        fields = '__all__'


class YouTubeVideoReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTubeVideoReaction
        fields = '__all__'
