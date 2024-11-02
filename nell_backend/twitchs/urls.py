from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

urlpatterns = [
    path('live-actions/', TwitchLiveActionViewSet.as_view({'get': 'list', 'post': 'create'}), name='twitch-live-action-list'),
    path('live-actions/<int:pk>/', TwitchLiveActionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='twitch-live-action-detail'),
    
    path('bluesky-reactions/', BlueskyPostReactionViewSet.as_view({'get': 'list', 'post': 'create'}), name='bluesky-post-reaction-list'),
    path('bluesky-reactions/<int:pk>/', BlueskyPostReactionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='bluesky-post-reaction-detail'),
    
    path('twitch-follower-actions/', TwitchFollowerActionViewSet.as_view({'get': 'list', 'post': 'create'}), name='twitch-follower-action-list'),
    path('twitch-follower-actions/<int:pk>/', TwitchFollowerActionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='twitch-follower-action-detail'),
    
    path('spotify-playlist-reactions/', SpotifyPlaylistAddSongReactionViewSet.as_view({'get': 'list', 'post': 'create'}), name='spotify-playlist-reaction-list'),
    path('spotify-playlist-reactions/<int:pk>/', SpotifyPlaylistAddSongReactionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='spotify-playlist-reaction-detail'),

    path('check-twitch-live/', CheckTwitchLiveView.as_view(), name='check-twitch-live'),
    path('bluesky/get-user-id/', GetBlueskyUserIDView.as_view(), name='get-bluesky-user-id'),
    path('check-twitch-follower/', TwitchFollowerActionViewSet.as_view({'get': 'list'}), name='check-twitch-follower'),
    path('spotify/get-playlist-id/', SpotifyPlaylistAddSongReactionViewSet.as_view({'get': 'list'}), name='get-spotify-playlist-id'),
]
