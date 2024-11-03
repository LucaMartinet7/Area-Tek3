from django.urls import path
from .views import YouTubeWatchActionView, GoogleCalendarCreateActionView

urlpatterns = [
    path('youtube-watch-action/', YouTubeWatchActionView.as_view(), name='youtube-watch-action'),
    path('google-calendar-create-action/', GoogleCalendarCreateActionView.as_view(), name='google-calendar-create-action'),
]
