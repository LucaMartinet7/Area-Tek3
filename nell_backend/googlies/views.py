from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import GmailReceivedAction, TwitchChatReaction, SpotifySongReaction
from .serializers import GmailReceivedActionSerializer, GmailCheckRequestSerializer
from .tasks import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth.models import AnonymousUser
from authentication.models import SocialUser


class GmailReceivedActionViewSet(viewsets.ModelViewSet):
    queryset = GmailReceivedAction.objects.all()
    serializer_class = GmailReceivedActionSerializer

    def get_queryset(self):
        user = self.request.user
        if isinstance(user, AnonymousUser):
            return GmailReceivedAction.objects.none()  # Return an empty queryset
        return self.queryset.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SetGmailTriggerView(APIView):
    @swagger_auto_schema(
        request_body=GmailCheckRequestSerializer,
        responses={200: openapi.Response('Gmail trigger saved successfully.')}
    )
    def post(self, request):
        print("Received POST request in SetGmailTriggerView")

        # Serialize request data
        serializer = GmailCheckRequestSerializer(data=request.data)
        print("Serializer initialized with data:", request.data)
        
        if not serializer.is_valid():
            print("Serializer validation failed with errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Extract validated data
        channel_name = serializer.validated_data.get("channel_name")
        message_content = serializer.validated_data.get("message_content")
        song_uri = serializer.validated_data.get("song_uri")
        print("Extracted channel_name:", channel_name)
        print("Extracted message_content:", message_content)
        print("Current user:", request.user)
        print("Provider filter:", 'gmail')
        # Find social user for Gmail
        social_user = SocialUser.objects.filter(user=request.user, provider='google').first()
        print("social_user:", social_user)
        if social_user:
            print(f"Found SocialUser with access_token: {social_user.access_token}")
        else:
            print("No SocialUser found for Gmail provider.")
            return Response({"error": "No Gmail social user found."}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            # Create GmailReceivedAction
            print("Creating GmailReceivedAction entry...")
            GmailReceivedAction.objects.create(
                user=request.user,
                #access_token=social_user.access_token,
            )
            print("GmailReceivedAction entry created successfully.")

            # Create TwitchChatReaction
            print("Creating TwitchChatReaction entry...")
            TwitchChatReaction.objects.create(
                user=request.user,
                channel_name=channel_name,
                message_content=message_content
            )
            print("TwitchChatReaction entry created successfully.")

            # Create SpotifySongReaction
            print("Creating SpotifySongReaction entry...")
            SpotifySongReaction.objects.create(
                user=request.user,
                song_uri=song_uri
            )
            print("SpotifySongReaction entry created successfully.")

            # Return success response
            print("All entries created successfully. Returning success response.")
            return Response({"message": "Gmail trigger saved successfully."}, status=status.HTTP_200_OK)

        except Exception as e:
            print("Exception occurred:", str(e))
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AREACheckGmailSpotify(APIView):
    def post(self, request):
        if check_gmail_for_spotify() == 0: 
            return Response({"message": "Gmail status check executed successfully."}, status=status.HTTP_200_OK)
        else:
            return Response("error: status 500" , status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class AREACheckGmailTwitch(APIView):
    def post(self, request):
        if check_gmail_for_twitch() == 0: 
            return Response({"message": "Gmail status check executed successfully."}, status=status.HTTP_200_OK)
        else:
            return Response("error: status 500" , status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class CheckGmailNew(APIView):
    def post(self, request):
        user = request.user
        if check_gmail_for_emails() == 0:
            return Response({"message": "Gmail status check executed successfully."}, status=status.HTTP_200_OK)
        else:
            return Response("error: status 500" , status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RunSpotifyReaction(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        user = request.user
        if run_spotify_reaction(user) == 0: 
            return Response({"message": "Spotify reaction executed successfully."}, status=status.HTTP_200_OK)
        else:
            return Response("error: status 500" , status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class RunTwitchReaction(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        user = request.user
        print(f"run_twitch_reaction return code: {run_twitch_reaction(user)}")
        if run_twitch_reaction(user) == 0:
            return Response({"message": "Twitch reaction executed successfully."}, status=status.HTTP_200_OK)
        else:
            return Response("error: status 500" , status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        