from django.db import models
from django.contrib.auth.models import User

class SpotifyAction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track_name = models.CharField(max_length=255)
    artist_name = models.CharField(max_length=255)
    spotify_user_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.artist_name}: {self.track_name}"
