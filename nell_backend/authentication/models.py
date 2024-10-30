from django.contrib.auth.models import User
from django.db import models

class SocialUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider_username = models.CharField(max_length=255, blank=True, null=True)
    provider = models.CharField(max_length=50)
    provider_id = models.CharField(max_length=255)  # Unique ID from provider
    access_token = models.CharField(max_length=255)
    
    class Meta:
        unique_together = ( 'provider_username', 'provider', 'provider_id')  # Ensures each provider ID is unique
