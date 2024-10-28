import requests
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TwitchLiveAction, BlueskyPostReaction
from .serializers import TwitchLiveActionSerializer, BlueskyPostReactionSerializer, BlueskyUserIDRequestSerializer
from .tasks import check_twitch_live
from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from atproto import Client

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

class GetBlueskyUserIDView(APIView):
    @swagger_auto_schema(
        request_body=BlueskyUserIDRequestSerializer,
        responses={200: openapi.Response('Bluesky User ID retrieved and saved successfully.')}
    )
    def post(self, request):
        serializer = BlueskyUserIDRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        bluesky_handle = serializer.validated_data.get("bluesky_handle")
        bluesky_password = serializer.validated_data.get("bluesky_password")

        try:
            # Initialize the Bluesky client and log in
            client = Client()
            login_response = client.login(bluesky_handle, bluesky_password)

            # Check if the login was successful and attempt to retrieve the user ID (DID)
            access_token = getattr(client, 'access_token', None)

            if not access_token and hasattr(client, 'session'):
                access_token = client.session.get('accessJwt', None)

            # Retrieve the Bluesky user ID (DID)
            user_profile = client.get_profile(actor=bluesky_handle)
            bluesky_user_id = user_profile.did

            if bluesky_user_id:
                # Save the details to BlueskyPostReaction table
                BlueskyPostReaction.objects.create(
                    user=request.user,
                    bluesky_handle=bluesky_handle,
                    bluesky_password=bluesky_password,
                    bluesky_user_id=bluesky_user_id
                )
                return Response({"bluesky_user_id": bluesky_user_id}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "User ID not found."}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)