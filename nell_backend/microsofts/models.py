from django.db import models
from django.contrib.auth.models import User

class OutlookReaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    recipient_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Outlook Email to {self.recipient_email} - {self.subject}"
