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

class TeamsMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_id = models.CharField(max_length=255, unique=True)
    subject = models.CharField(max_length=255)
    body_preview = models.TextField()
    received_at = models.DateTimeField()
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f"Message {self.message_id} for {self.user}"

class CalendarEventReaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    summary = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Calendar Event for {self.user} - {self.summary}"