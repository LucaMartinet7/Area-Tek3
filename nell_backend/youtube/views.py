from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import YouTubeWatchAction, CalendarEventReaction
from .serializers import YouTubeWatchActionSerializer, CalendarEventReactionSerializer
from .tasks import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from authentication.models import SocialUser
from django.contrib.auth.models import AnonymousUser
import logging

logger = logging.getLogger(__name__)


class YouTubeWatchActionViewSet(viewsets.ModelViewSet):
    queryset = YouTubeWatchAction.objects.all()
    serializer_class = YouTubeWatchActionSerializer

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user) if not isinstance(user, AnonymousUser) else YouTubeWatchAction.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CalendarEventReactionViewSet(viewsets.ModelViewSet):
    queryset = CalendarEventReaction.objects.all()
    serializer_class = CalendarEventReactionSerializer

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user) if not isinstance(user, AnonymousUser) else CalendarEventReaction.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SetYouTubeTriggerView(APIView):
    """
    Triggered when a user watches a YouTube video.
    Creates a Google Calendar event based on that action.
    """
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        request_body=YouTubeWatchActionSerializer,
        responses={200: openapi.Response('YouTube trigger saved successfully.')}
    )
    def post(self, request):
        serializer = YouTubeWatchActionSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        social_user = SocialUser.objects.filter(user=request.user, provider='google').first()
        if not social_user:
            return Response({"error": "No Google social user found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            # Save YouTube watch action and trigger Google Calendar reaction
            serializer.save(user=request.user)
            create_google_calendar_event_for_youtube_watch(request.user)
            return Response({"message": "YouTube trigger saved successfully."}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error creating Google Calendar event for YouTube watch: {e}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SetCalendarEventTriggerView(APIView):
    """
    Triggered when a new Google Calendar event is created.
    Launches a YouTube video based on that action.
    """
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        request_body=CalendarEventReactionSerializer,
        responses={200: openapi.Response('Google Calendar trigger saved successfully.')}
    )
    def post(self, request):
        serializer = CalendarEventReactionSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        social_user = SocialUser.objects.filter(user=request.user, provider='youtube').first()
        if not social_user:
            return Response({"error": "No YouTube social user found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            # Save Calendar event action and trigger YouTube reaction
            serializer.save(user=request.user)
            launch_youtube_video_for_calendar_event(request.user)
            return Response({"message": "Google Calendar trigger saved successfully."}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error launching YouTube video for Calendar event: {e}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
