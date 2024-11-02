from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

urlpatterns = [
    path('gmail-received-action/', GmailReceivedActionViewSet.as_view({'get': 'list', 'post': 'create'}), name='gmail-received-action'),
    path('set-gmail-trigger/', SetGmailTriggerView.as_view(), name='set-gmail-trigger'),
    path('area-check-gmail-spotify/', AREACheckGmailSpotify.as_view(), name='check-gmail-spotify'),
    path('area-check-gmail-twitch/', AREACheckGmailTwitch.as_view(), name='check-gmail-twitch'),
    path('run-spotify-reaction/', RunSpotifyReaction.as_view(), name='run-spotify-reaction'),
    path('run-twitch-reaction/', RunTwitchReaction.as_view(), name='run-twitch-reaction'),
    path('check-for-new-emails/', CheckGmailNew.as_view(), name='check-for-new-emails'),
]
