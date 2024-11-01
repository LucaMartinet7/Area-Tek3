from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import GmailReceivedAction, TwitchChatReaction, SpotifySongReaction
from .serializers import GmailReceivedActionSerializer, GmailCheckRequestSerializer
from .tasks import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class GmailReceivedActionViewSet(viewsets.ModelViewSet):
    queryset = GmailReceivedAction.objects.all()
    serializer_class = GmailReceivedActionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SetGmailTriggerView(APIView):
    @swagger_auto_schema(
        request_body=GmailCheckRequestSerializer,
        responses={200: openapi.Response('Gmail trigger saved successfully.')}
    )
    def post(self, request):
        serializer = GmailCheckRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        access_token = serializer.validated_data.get("access_token")
        channel_name = serializer.validated_data.get("channel_name")
        message_content = serializer.validated_data.get("message_content")

        try:
            GmailReceivedAction.objects.create(
                user=request.user,
                access_token=access_token
            )
            TwitchChatReaction.objects.create(
                user=request.user,
                channel_name=channel_name,
                message_content=message_content
            )
            SpotifySongReaction.objects.create(
                user=request.user
            )
            return Response({"message": "Gmail trigger saved successfully."}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CheckGmailSpotify(APIView):
    def post(self, request):
        if check_gmail_for_spotify() == 0: 
            return Response({"message": "Gmail status check executed successfully."}, status=status.HTTP_200_OK)
        else:
            return Response("error: status 500" , status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class CheckGmailTwitch(APIView):
    def post(self, request):
        if check_gmail_for_twitch() == 0: 
            return Response({"message": "Gmail status check executed successfully."}, status=status.HTTP_200_OK)
        else:
            return Response("error: status 500" , status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RunSpotifyReaction(APIView):
    def post(self, request):
        if run_spotify_reaction() == 0: 
            return Response({"message": "Spotify reaction executed successfully."}, status=status.HTTP_200_OK)
        else:
            return Response("error: status 500" , status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class RunTwitchReaction(APIView):
    def post(self, request):
        if run_twitch_reaction() == 0: 
            return Response({"message": "Twitch reaction executed successfully."}, status=status.HTTP_200_OK)
        else:
            return Response("error: status 500" , status=status.HTTP_500_INTERNAL_SERVER_ERROR)