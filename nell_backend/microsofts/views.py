import requests
import msal
from django.conf import settings
from django.shortcuts import redirect, render
from django.http import JsonResponse
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import OutlookReaction
from .serializers import OutlookReactionSerializer

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

def microsoft_login(request):
    client = msal.ConfidentialClientApplication(
        settings.MICROSOFT_CLIENT_ID,
        authority=settings.MICROSOFT_AUTHORITY,
        client_credential=settings.MICROSOFT_CLIENT_SECRET
    )
    
    auth_url = client.get_authorization_request_url(
        settings.MICROSOFT_SCOPE,
        redirect_uri=settings.MICROSOFT_REDIRECT_URI
    )
    return redirect(auth_url)

def microsoft_callback(request):
    code = request.GET.get('code')
    
    if not code:
        return JsonResponse({'error': 'No code provided'}, status=400)
    
    client = msal.ConfidentialClientApplication(
        settings.MICROSOFT_CLIENT_ID,
        authority=settings.MICROSOFT_AUTHORITY,
        client_credential=settings.MICROSOFT_CLIENT_SECRET
    )
    
    token_response = client.acquire_token_by_authorization_code(
        code,
        scopes=settings.MICROSOFT_SCOPE,
        redirect_uri=settings.MICROSOFT_REDIRECT_URI
    )
    
    if 'access_token' in token_response:
        request.session['microsoft_access_token'] = token_response['access_token']
        request.session['microsoft_refresh_token'] = token_response['refresh_token']
        
        return JsonResponse({
            'access_token': token_response['access_token'],
            'refresh_token': token_response['refresh_token'],
            'expires_in': token_response['expires_in']
        })
    else:
        return JsonResponse({'error': 'Failed to acquire access token', 'details': token_response}, status=400)

def get_user_info(request):
    access_token = request.session.get('microsoft_access_token')
    
    if not access_token:
        return JsonResponse({'error': 'User not authenticated'}, status=401)
    
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    
    graph_url = 'https://graph.microsoft.com/v1.0/me'
    response = requests.get(graph_url, headers=headers)
    
    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({'error': 'Failed to fetch user info'}, status=response.status_code)
