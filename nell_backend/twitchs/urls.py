from django.urls import path, include
from .views import twitch_login, twitch_callback, get_twitch_user
from rest_framework.routers import DefaultRouter
from .views import TwitchLiveActionViewSet, BlueskyPostReactionViewSet

router = DefaultRouter()
router.register(r'live-actions', TwitchLiveActionViewSet, basename='twitch-live-action')
router.register(r'bluesky-reactions', BlueskyPostReactionViewSet, basename='bluesky-post-reaction')

urlpatterns = [
    path('login/', twitch_login, name='twitch_login'),
    path('callback/', twitch_callback, name='twitch_callback'),
    path('user/', get_twitch_user, name='get_user_info'),
    path('', include(router.urls)),
]
