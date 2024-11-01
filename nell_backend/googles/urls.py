from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GmailReceivedActionViewSet, SetGmailTriggerView, CheckGmailSpotify, CheckGmailTwitch, RunSpotifyReaction, RunTwitchReaction

router = DefaultRouter()
router.register(r'gmail-actions', GmailReceivedActionViewSet, basename='gmail-action')

urlpatterns = [
    path('', include(router.urls)),
    path('set-gmail-trigger/', SetGmailTriggerView.as_view(), name='set-gmail-trigger'),
    path('check-gmail-spotify/', CheckGmailSpotify.as_view(), name='check-gmail-spotify'),
    path('check-gmail-twitch/', CheckGmailTwitch.as_view(), name='check-gmail-twitch'),
    path('run-spotify-reaction/', RunSpotifyReaction, name='run-spotify-reaction'),
    path('run-twitch-reaction/', RunTwitchReaction, name='run-twitch-reaction'),
]
