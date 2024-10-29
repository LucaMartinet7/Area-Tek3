import requests
import msal
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect, render
from django.http import JsonResponse
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from .tasks import check_teams_message, check_onedrive_for_new_file

def send_outlook_email(user):
    email_data = {
        "subject": "You're listening to The Beatles!",
        "body": "Hey, we noticed you're playing a Beatles song on Spotify!",
        "recipient_email": "recipient@example.com"
    }

    access_token = "your_microsoft_access_token"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    email_payload = {
        "message": {
            "subject": email_data["subject"],
            "body": {
                "contentType": "Text",
                "content": email_data["body"]
            },
            "toRecipients": [
                {
                    "emailAddress": {
                        "address": email_data["recipient_email"]
                    }
                }
            ]
        },
        "saveToSentItems": "true"
    }

    response = requests.post(
        'https://graph.microsoft.com/v1.0/me/sendMail',
        headers=headers,
        json=email_payload
    )

    if response.status_code == 202:
        OutlookReaction.objects.create(
            user=user,
            subject=email_data["subject"],
            body=email_data["body"],
            recipient_email=email_data["recipient_email"]
        )
    else:
        raise Exception("Failed to send email")

class OutlookReactionViewSet(viewsets.ModelViewSet):
    queryset = OutlookReaction.objects.all()
    serializer_class = OutlookReactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TriggerOutlookEmailAPIView(APIView):
    def post(self, request):
        try:
            send_outlook_email(request.user)
            return Response({"message": "Outlook email sent successfully."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TeamsMessageCheckAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            user = request.user
            access_token = request.data.get("access_token")
            check_teams_message(user.id, access_token)
            return Response({"message": "Teams message check complete."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TeamsMessageViewSet(viewsets.ModelViewSet):
    queryset = TeamsMessage.objects.all()
    serializer_class = TeamsMessageSerializer
    permission_classes = [permissions.IsAuthenticated]

class CalendarEventReactionViewSet(viewsets.ModelViewSet):
    queryset = CalendarEventReaction.objects.all()
    serializer_class = CalendarEventReactionSerializer
    permission_classes = [permissions.IsAuthenticated]

class TriggerOneDriveToGoogleDriveSync(APIView):
    def post(self, request):
        user_id = request.user.id
        access_token = request.data.get('access_token')

        check_onedrive_for_new_file(user_id, access_token)
        return Response({"message": "OneDrive to Google Drive sync triggered."}, status=status.HTTP_200_OK)

class GoogleDriveFileReactionViewSet(viewsets.ModelViewSet):
    queryset = GoogleDriveFileReaction.objects.all()
    serializer_class = GoogleDriveFileReactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class OutlookEmailActionViewSet(viewsets.ModelViewSet):
    queryset = OutlookEmailAction.objects.all()
    serializer_class = OutlookEmailActionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class GoogleChatMessageReactionViewSet(viewsets.ModelViewSet):
    queryset = GoogleChatMessageReaction.objects.all()
    serializer_class = GoogleChatMessageReactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
class OutlookEmailActionViewSet(viewsets.ModelViewSet):
    queryset = OutlookEmailAction.objects.all()
    serializer_class = OutlookEmailActionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class GoogleChatMessageReactionViewSet(viewsets.ModelViewSet):
    queryset = GoogleChatMessageReaction.objects.all()
    serializer_class = GoogleChatMessageReactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
