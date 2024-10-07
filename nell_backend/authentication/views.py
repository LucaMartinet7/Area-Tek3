from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from allauth.socialaccount.providers.oauth2.client import OAuth2Error
from allauth.socialaccount.models import SocialToken, SocialApp, SocialAccount
from django.contrib.auth.models import User
from .models import UserToken
from .serializers import UserTokenSerializer
import requests

class OAuthLoginView(APIView):
    def get(self, request, provider):
        try:
            app = SocialApp.objects.get(provider=provider)
            login_url = f"/accounts/{provider}/login/"
            return Response({'login_url': login_url})
        except SocialApp.DoesNotExist:
            return Response({'error': 'Provider not configured'}, status=404)

class OAuthCallbackView(APIView):
    """
    Handles the callback after the user logs in with their social account.
    Stores the access token in the database.
    """

    def post(self, request, *args, **kwargs):
        provider = request.data.get('provider')
        code = request.data.get('code')

        try:
            app = SocialApp.objects.get(provider=provider)
            token_url = app.token_url
            redirect_uri = app.callback_url

            payload = {
                'client_id': app.client_id,
                'client_secret': app.secret,
                'code': code,
                'redirect_uri': redirect_uri,
                'grant_type': 'authorization_code',
            }

            response = requests.post(token_url, data=payload)
            token_data = response.json()

            # Create or update the UserToken instance
            user = request.user
            token, _ = UserToken.objects.update_or_create(
                user=user,
                provider=provider,
                defaults={
                    'access_token': token_data['access_token'],
                    'refresh_token': token_data.get('refresh_token'),
                    'expires_at': token_data.get('expires_in'),
                }
            )

            serializer = UserTokenSerializer(token)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except OAuth2Error as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except SocialApp.DoesNotExist:
            return Response({'error': 'Invalid provider'}, status=status.HTTP_400_BAD_REQUEST)
