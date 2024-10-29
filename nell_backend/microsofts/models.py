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
    
class OneDriveFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    saved_to_drive = models.BooleanField(default=False)

    def __str__(self):
        return f"OneDrive File: {self.name}"

class GoogleDriveFileReaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    google_drive_id = models.CharField(max_length=255)
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Google Drive File: {self.file_name}"

class OutlookEmailAction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    sender = models.EmailField()
    received_at = models.DateTimeField()
    message_id = models.CharField(max_length=255, unique=True)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f"Outlook Email from {self.sender} - {self.subject}"

class GoogleChatMessageReaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat_space = models.CharField(max_length=255)
    email_subject = models.CharField(max_length=255)
    email_sender = models.EmailField()
    message_id = models.CharField(max_length=255)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Google Chat Message: {self.email_subject} (Posted in {self.chat_space})"
    
