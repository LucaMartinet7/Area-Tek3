from django.db import models
from django.contrib.auth.models import User

class GmailReceivedAction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Gmail Received Action"


class TwitchChatReaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel_name = models.CharField(max_length=255)
    message_content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Twitch Chat Message: {self.message_content}"


class SpotifySongReaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song_uri = models.CharField(max_length=100, default="spotify:track:4KYS9GK68yeuUJ8vJfPxrq")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Spotify Song Reaction"
