from rest_framework import serializers
from .models import GmailReceivedAction, TwitchChatReaction, SpotifySongReaction

class GmailReceivedActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GmailReceivedAction
        fields = '__all__'

class TwitchChatReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitchChatReaction
        fields = '__all__'

class SpotifySongReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifySongReaction
        fields = '__all__'

class GmailCheckRequestSerializer(serializers.Serializer):
    song_uri = serializers.CharField(max_length=255)
    channel_name = serializers.CharField(max_length=255)
    message_content = serializers.CharField(max_length=500)
