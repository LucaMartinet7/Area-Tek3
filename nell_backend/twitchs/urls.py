from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TwitchLiveActionViewSet, BlueskyPostReactionViewSet, CheckTwitchLiveView, GetBlueskyUserIDView

router = DefaultRouter()
router.register(r'live-actions', TwitchLiveActionViewSet, basename='twitch-live-action')
router.register(r'bluesky-reactions', BlueskyPostReactionViewSet, basename='bluesky-post-reaction')

urlpatterns = [
    path('', include(router.urls)),
    path('check-twitch-live/', CheckTwitchLiveView.as_view(), name='check-twitch-live'),
    path('bluesky/get-user-id/', GetBlueskyUserIDView.as_view(), name='get-bluesky-user-id'),
]
