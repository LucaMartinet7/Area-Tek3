from django.db import models
from django.contrib.auth.models import User

class YouTubeWatchAction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Watched YouTube Video: {self.video_id}"


class GoogleCalendarEventReaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_title = models.CharField(max_length=255)
    event_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Google Calendar Event: {self.event_title}"


class GoogleCalendarCreateAction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Created Google Calendar Event: {self.event_id}"


class YouTubeVideoReaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Launched YouTube Video: {self.video_id}"
