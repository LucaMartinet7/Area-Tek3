from django.contrib.auth.models import User
from django.db import models

class Service(models.Model):
    GOOGLE = 'google'
    DISCORD = 'discord'
    GITHUB = 'github'
    MICROSOFT = 'microsoft'
    OPEN_WEATHER = 'open_weather'
    SPOTIFY = 'spotifys'
    TWITCH = 'twitchs'
    YOUTUBE = 'youtube'

    SERVICE_CHOICES = [
        (GOOGLE, 'Google'),
        (DISCORD, 'Discord'),
        (GITHUB, 'GitHub'),
        (MICROSOFT, 'Microsoft'),
        (OPEN_WEATHER, 'Open Weather'),
        (SPOTIFY, 'Spotify'),
        (TWITCH, 'Twitch'),
        (YOUTUBE, 'YouTube'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255, blank=True, null=True)
    expires_in = models.DateTimeField()  # Token expiration time
    token_type = models.CharField(max_length=50)
    additional_info = models.JSONField(blank=True, null=True)  # Store additional data if needed

    def __str__(self):
        return f"{self.user.username}'s {self.service_type.capitalize()} Account"
