from rest_framework import serializers
from .models import OutlookReaction

class OutlookReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutlookReaction
        fields = '__all__'
