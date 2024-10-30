import requests
from urllib.parse import urlencode
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string  # Import for generating fallback usernames
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import SocialUser
from .serializers import RegisterSerializer, LoginSerializer, SocialUserSerializer

# OAuth configuration for each provider from settings
PROVIDERS = {
    'discord': {
        'client_id': settings.SOCIAL_AUTH_DISCORD_KEY,
        'client_secret': settings.SOCIAL_AUTH_DISCORD_SECRET,
        'auth_url': 'https://discord.com/api/oauth2/authorize',
        'token_url': 'https://discord.com/api/oauth2/token',
        'data_url': 'https://discord.com/api/users/@me',
        'scope': 'identify',
    },
    'github': {
        'client_id': settings.SOCIAL_AUTH_GITHUB_KEY,
        'client_secret': settings.SOCIAL_AUTH_GITHUB_SECRET,
        'auth_url': 'https://github.com/login/oauth/authorize',
        'token_url': 'https://github.com/login/oauth/access_token',
        'data_url': 'https://api.github.com/user',
        'scope': 'user',
    },
    'google': {
        'client_id': settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
        'client_secret': settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
        'auth_url': 'https://accounts.google.com/o/oauth2/auth',
        'token_url': 'https://oauth2.googleapis.com/token',
        'data_url': 'https://www.googleapis.com/oauth2/v1/userinfo',
        'scope': 'https://www.googleapis.com/auth/userinfo.profile',
    },
    'reddit': {
        'client_id': settings.REDDIT_CLIENT_ID,
        'client_secret': settings.REDDIT_CLIENT_SECRET,
        'auth_url': 'https://www.reddit.com/api/v1/authorize',
        'token_url': 'https://www.reddit.com/api/v1/access_token',
        'data_url': 'https://oauth.reddit.com/api/v1/me',
        'scope': 'identity',
    },
    'spotify': {
        'client_id': settings.SPOTIFY_CLIENT_ID,
        'client_secret': settings.SPOTIFY_CLIENT_SECRET,
        'auth_url': 'https://accounts.spotify.com/authorize',
        'token_url': 'https://accounts.spotify.com/api/token',
        'data_url': 'https://api.spotify.com/v1/me',
        'scope': 'user-read-private',
    },
    'twitch': {
        'client_id': settings.TWITCH_CLIENT_ID,
        'client_secret': settings.TWITCH_CLIENT_SECRET,
        'auth_url': 'https://id.twitch.tv/oauth2/authorize',
        'token_url': 'https://id.twitch.tv/oauth2/token',
        'data_url': 'https://api.twitch.tv/helix/users',
        'scope': 'user:read:email',
    },
}

# Internal callback URI for backend processing
INTERNAL_REDIRECT_URI = 'http://localhost:3000/dashboard'  # Replace with your server address if hosted

class RegisterView(APIView):
    @swagger_auto_schema(
        request_body=RegisterSerializer,
        responses={201: "User registered successfully", 400: "Bad Request"},
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={200: "User logged in successfully", 400: "Invalid credentials"},
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({"message": "User logged in successfully", "username": user.username}, status=status.HTTP_200_OK)
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OAuthInitView(APIView):
    """
    Initiates the OAuth flow by redirecting to the provider's authorization page.
    """
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'provider', openapi.IN_PATH, description="OAuth provider (discord, github, google, reddit, spotify, twitch)", type=openapi.TYPE_STRING
            )
        ],
        responses={302: "Redirect to provider's OAuth authorization URL", 400: "Unsupported provider"}
    )
    def get(self, request, provider):
        if provider not in PROVIDERS:
            return Response({"error": "Unsupported provider"}, status=status.HTTP_400_BAD_REQUEST)
        
        provider_config = PROVIDERS[provider]
        params = {
            'client_id': provider_config['client_id'],
            'redirect_uri': INTERNAL_REDIRECT_URI.format(provider=provider),
            'response_type': 'code',
            'scope': provider_config['scope'],
        }
        auth_url = f"{provider_config['auth_url']}?{urlencode(params)}"
        return HttpResponseRedirect(auth_url)

class OAuthCallbackView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'provider', openapi.IN_PATH, description="OAuth provider (github, google, etc.)", type=openapi.TYPE_STRING
            )
        ],
        responses={302: "User logged in or linked successfully", 400: "Unsupported provider or missing authorization code"}
    )
    @csrf_exempt
    def get(self, request, provider):
        if provider not in PROVIDERS:
            return Response({"error": "Unsupported provider"}, status=status.HTTP_400_BAD_REQUEST)

        code = request.GET.get('code')
        if not code:
            return Response({"error": "Authorization code not provided"}, status=status.HTTP_400_BAD_REQUEST)

        provider_config = PROVIDERS[provider]

        # Exchange authorization code for access token
        token_data = {
            'client_id': provider_config['client_id'],
            'client_secret': provider_config['client_secret'],
            'code': code,
            'redirect_uri': INTERNAL_REDIRECT_URI.format(provider=provider),
            'grant_type': 'authorization_code',
        }
        token_response = requests.post(provider_config['token_url'], data=token_data, headers={'Accept': 'application/json'})
        token_response.raise_for_status()
        access_token = token_response.json().get('access_token')

        # Retrieve user data
        headers = {'Authorization': f"Bearer {access_token}"}
        data_response = requests.get(provider_config['data_url'], headers=headers)
        data_response.raise_for_status()
        user_data = data_response.json()

        provider_id = user_data.get('id')
        provider_username = user_data.get('login')
        email = user_data.get('email')
        username = provider_username or email or get_random_string(10)

        # Check if user is already authenticated
        if request.user.is_authenticated:
            user = request.user
            social_user, created = SocialUser.objects.get_or_create(
                user=user, provider=provider, provider_id=provider_id,
                defaults={'access_token': access_token, 'provider_username': username}
            )
            if not created:
                social_user.access_token = access_token
                social_user.provider_username = username
                social_user.save()
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

        # Save info before redirecting
        try:
            social_user = SocialUser.objects.get(provider=provider, provider_id=provider_id)
            user = social_user.user
            social_user.access_token = access_token
            social_user.provider_username = username
            social_user.save()
        except SocialUser.DoesNotExist:
            user = User.objects.create(username=username, email=email)
            social_user = SocialUser.objects.create(
                user=user, provider=provider, provider_id=provider_id,
                access_token=access_token, provider_username=username
            )

        # Authenticate and log in
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')

        # Redirect to the specified LOGIN_REDIRECT_URL
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)