from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

urlpatterns = [
# Individual APIView endpoints
    path('check-twitch-live/', ChannelStatusCheckView.as_view(), name='check-twitch-live'),
    path('post-to-bluesky/', PostToBlueskyView.as_view(), name='post-to-bluesky'),
    path('setup-bluesky-user/', GetBlueskyUserIDView.as_view(), name='setup-bluesky-user'),
    path('check-and-post-to-bluesky/', CheckAndPostToBlueskyView.as_view(), name='check-and-post-to-bluesky'),
    
    # Manually defined paths for ViewSet actions
    path('twitch-live-actions/', TwitchLiveActionViewSet.as_view({'get': 'list', 'post': 'create'}), name='twitch-live-action-list'),
    path('twitch-live-actions/<int:pk>/', TwitchLiveActionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='twitch-live-action-detail'),

    path('bluesky-post-reactions/', BlueskyPostReactionViewSet.as_view({'get': 'list', 'post': 'create'}), name='bluesky-post-reaction-list'),
    path('bluesky-post-reactions/<int:pk>/', BlueskyPostReactionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='bluesky-post-reaction-detail'),
]
