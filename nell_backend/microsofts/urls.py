from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'reactions', OutlookReactionViewSet)
router.register(r'teams-messages', TeamsMessageViewSet)
router.register(r'calendar-events', CalendarEventReactionViewSet)
router.register(r'drive-file-reactions', GoogleDriveFileReactionViewSet)
router.register(r'outlook-email-actions', OutlookEmailActionViewSet)
router.register(r'google-chat-reactions', GoogleChatMessageReactionViewSet)

urlpatterns = [
    path('trigger-email/', TriggerOutlookEmailAPIView.as_view(), name='trigger_outlook_email'),
    path('check-teams-message/', TeamsMessageCheckAPIView.as_view(), name='check_teams_message'),
    path('trigger-onedrive-sync/', TriggerOneDriveToGoogleDriveSync.as_view(), name='trigger_onedrive_sync'),
    path('check-outlook-email/', OutlookEmailActionViewSet.as_view(), name='check_outlook_email'),
    path('trigger-google-chat/', GoogleChatMessageReactionViewSet.as_view(), name='trigger_google_chat'),
    path('', include(router.urls)),
]
