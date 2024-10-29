from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OutlookReactionViewSet, TriggerOutlookEmailAPIView, TeamsMessageViewSet, CalendarEventReactionViewSet, TeamsMessageCheckAPIView

router = DefaultRouter()
router.register(r'reactions', OutlookReactionViewSet)
router.register(r'teams-messages', TeamsMessageViewSet)
router.register(r'calendar-events', CalendarEventReactionViewSet)

urlpatterns = [
    path('trigger-email/', TriggerOutlookEmailAPIView.as_view(), name='trigger_outlook_email'),
    path('check-teams-message/', TeamsMessageCheckAPIView.as_view(), name='check_teams_message'),
    path('', include(router.urls)),
]
