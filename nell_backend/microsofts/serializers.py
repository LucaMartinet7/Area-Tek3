from rest_framework import serializers
from .models import *

class OutlookReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutlookReaction
        fields = '__all__'

class TeamsMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamsMessage
        fields = '__all__'

class CalendarEventReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarEventReaction
        fields = '__all__'

class GoogleDriveFileReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleDriveFileReaction
        fields = '__all__'
