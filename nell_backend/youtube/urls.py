from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CheckYouTubeVideoUploadView, CheckYouTubeWatchView, YouTubeActionViewSet, SpotifyPlaylistReactionViewSet, YouTubeChannelSetupView

router = DefaultRouter()
router.register(r'youtube-actions', YouTubeActionViewSet, basename='youtube-action')
router.register(r'spotify-reactions', SpotifyPlaylistReactionViewSet, basename='spotify-reaction')

urlpatterns = [
    path('', include(router.urls)),
    path('check-youtube-upload/', CheckYouTubeVideoUploadView.as_view(), name='check_youtube_upload'),
    path('check-youtube-watch/', CheckYouTubeWatchView.as_view(), name='check_youtube_watch'),
    path('setup-youtube-channel/', YouTubeChannelSetupView.as_view(), name='setup_youtube_channel'),
]
