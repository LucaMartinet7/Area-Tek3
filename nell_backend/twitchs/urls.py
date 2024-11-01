from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'live-actions', TwitchLiveActionViewSet, basename='twitch-live-action')
router.register(r'bluesky-reactions', BlueskyPostReactionViewSet, basename='bluesky-post-reaction')
router.register(r'twitch-follower-actions', TwitchFollowerActionViewSet, basename='twitch-follower-action')
router.register(r'spotify-playlist-reactions', SpotifyPlaylistAddSongReactionViewSet, basename='spotify-playlist-reaction')

urlpatterns = [
    path('', include(router.urls)),
    path('check-twitch-live/', CheckTwitchLiveView.as_view(), name='check-twitch-live'),
    path('bluesky/get-user-id/', GetBlueskyUserIDView.as_view(), name='get-bluesky-user-id'),
    path('check-twitch-follower/', TwitchFollowerActionViewSet.as_view(), name='check-twitch-follower'),
    path('spotify/get-playlist-id/', SpotifyPlaylistAddSongReactionViewSet.as_view(), name='get-spotify-playlist-id'),
]
