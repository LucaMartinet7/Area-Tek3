from django.db import models
from django.contrib.auth.models import User

class YouTubeAction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel_id = models.CharField(max_length=255)
    video_id = models.CharField(max_length=255, blank=True, null=True)
    milestone_views = models.IntegerField(default=10000)
    api_key = models.CharField(max_length=255, blank=True, null=True)
    last_view_count = models.IntegerField(default=0)
    action_type = models.CharField(max_length=50, choices=[('upload', 'Upload'), ('subscription', 'Subscription')])
    last_checked = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - YouTube Action: {self.action_type} for {self.channel_id}"

class SpotifyPlaylistReaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    playlist_id = models.CharField(max_length=255, blank=True, null=True)
    playlist_name = models.CharField(max_length=255)
    spotify_user_id = models.CharField(max_length=255, blank=True, null=True)
    access_token = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Spotify Playlist: {self.playlist_name}"
