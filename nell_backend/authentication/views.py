from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from allauth.socialaccount.providers.oauth2.client import OAuth2Error
from allauth.socialaccount.models import SocialToken, SocialApp, SocialAccount
from dj_rest_auth.registration.serializers import RegisterSerializer
from drf_yasg.utils import swagger_auto_schema
from .models import UserToken
from .serializers import UserTokenSerializer

import requests

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    @swagger_auto_schema(request_body=RegisterSerializer)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)

class OAuthLoginView(APIView):
    def get(self, request, provider):
        try:
            app = SocialApp.objects.get(provider=provider)
            # Use a Flutter deep link or web URL that your Flutter app handles for OAuth login
            flutter_login_url = f"your_flutter_app://login/{provider}"  # Replace with the actual Flutter deep link
            return Response({'login_url': flutter_login_url})
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
            flutter_redirect_url = "http://localhost:3000/dashboard"  # Replace with your actual Flutter URL

            payload = {
                'client_id': app.client_id,
                'client_secret': app.secret,
                'code': code,
                'redirect_uri': flutter_redirect_url,  # Use Flutter URL as redirect URI
                'grant_type': 'authorization_code',
            }

            response = requests.post(token_url, data=payload)
            token_data = response.json()

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
