from django.db import models
from django.contrib.auth.models import User

class TwitchLiveAction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel_name = models.CharField(max_length=255)
    twitch_user_id = models.CharField(max_length=255, blank=True, null=True)
    access_token = models.CharField(max_length=255, blank=True, null=True)
    client_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Twitch Channel Live: {self.channel_name}"

class BlueskyPostReaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    bluesky_handle = models.CharField(max_length=255, default='')
    bluesky_user_id = models.CharField(max_length=255, blank=True, null=True)
    bluesky_password = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Bluesky Post: {self.message}"
