import requests
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TwitchLiveAction, BlueskyPostReaction
from .serializers import TwitchLiveActionSerializer, BlueskyPostReactionSerializer
from .tasks import check_twitch_live

class CheckTwitchLiveView(APIView):
    def post(self, request):
        try:
            check_twitch_live()
            return Response({"message": "Twitch live status check executed successfully."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TwitchLiveActionViewSet(viewsets.ModelViewSet):
    queryset = TwitchLiveAction.objects.all()
    serializer_class = TwitchLiveActionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BlueskyPostReactionViewSet(viewsets.ModelViewSet):
    queryset = BlueskyPostReaction.objects.all()
    serializer_class = BlueskyPostReactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
