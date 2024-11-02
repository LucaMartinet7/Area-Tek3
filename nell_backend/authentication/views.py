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
from django.contrib.auth.models import AnonymousUser

from .models import SocialUser, PersistentToken
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer

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
        'scope': 'https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/gmail.readonly',
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
        'scope': 'user-read-email user-modify-playback-state user-read-playback-state user-read-currently-playing',
    },
    'twitch': {
        'client_id': settings.TWITCH_CLIENT_ID,
        'client_secret': settings.TWITCH_CLIENT_SECRET,
        'auth_url': 'https://id.twitch.tv/oauth2/authorize',
        'token_url': 'https://id.twitch.tv/oauth2/token',
        'data_url': 'https://api.twitch.tv/helix/users',
        'user_id': 'https://api.twitch.tv/helix/users?login=<username>',
        'scope': 'user:read:email chat:edit chat:read user:write:chat',
    },
}

# Base callback URI with a placeholder for the provider
INTERNAL_REDIRECT_URI_TEMPLATE = 'http://127.0.0.1:8000/api/auth/{provider}/callback/'
TWITCH_REDIRECT_URI = settings.TWITCH_REDIRECT_URI

class UserInfoView(APIView): #add providers
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            has_token = PersistentToken.user_has_token(user)
            return Response({
                "username": user.username,
                "email": user.email,
                "has_token": has_token
            }, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            token, created = PersistentToken.objects.get_or_create(user=user)
            return Response({"token": str(token.token)}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    @swagger_auto_schema(...)
    def post(self, request):
        print("Registering new user with data:", request.data)
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            PersistentToken.objects.create(user=user)
            print("User registered successfully:", user)
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        print("Registration errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    @swagger_auto_schema(...)
    def post(self, request):
        print("Attempting login with data:", request.data)
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            print("Authenticating user:", username)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print("User logged in successfully:", user.username)
                return Response({"message": "User logged in successfully", "username": user.username}, status=status.HTTP_200_OK)
            print("Invalid credentials for user:", username)
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        print("Login validation errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OAuthInitView(APIView):
    @swagger_auto_schema(manual_parameters=[openapi.Parameter('provider', openapi.IN_PATH, description="OAuth provider", type=openapi.TYPE_STRING)])
    def get(self, request, provider):
        if provider not in PROVIDERS:
            return Response({"error": "Unsupported provider"}, status=status.HTTP_400_BAD_REQUEST)

        provider_config = PROVIDERS[provider]
        
        # Use Twitch's specific redirect URI or default
        redirect_uri = TWITCH_REDIRECT_URI if provider == 'twitch' else INTERNAL_REDIRECT_URI_TEMPLATE.format(provider=provider)
        
        # Encode parameters, including redirect_uri
        params = {
            'client_id': provider_config['client_id'],
            'redirect_uri': redirect_uri,
            'response_type': 'code',
            'scope': provider_config['scope'],
        }
        
        # Properly build the auth URL
        auth_url = f"{provider_config['auth_url']}?{urlencode(params)}"
        return HttpResponseRedirect(auth_url)


class OAuthCallbackView(APIView):
    @swagger_auto_schema(manual_parameters=[openapi.Parameter('provider', openapi.IN_PATH, description="OAuth provider", type=openapi.TYPE_STRING)])
    @method_decorator(csrf_exempt, name='dispatch')
    def get(self, request, provider):
        if getattr(self, 'swagger_fake_view', False):
            return Response({"message": "Schema generation in progress"}, status=status.HTTP_200_OK)

        if provider not in PROVIDERS:
            return Response({"error": "Unsupported provider"}, status=status.HTTP_400_BAD_REQUEST)

        code = request.GET.get('code')
        if not code:
            return Response({"error": "Authorization code not provided"}, status=status.HTTP_400_BAD_REQUEST)

        provider_config = PROVIDERS[provider]
        redirect_uri = settings.TWITCH_REDIRECT_URI if provider == 'twitch' else INTERNAL_REDIRECT_URI_TEMPLATE.format(provider=provider)
        
        token_data = {
            'client_id': provider_config['client_id'],
            'client_secret': provider_config['client_secret'],
            'code': code,
            'redirect_uri': redirect_uri,
            'grant_type': 'authorization_code',
        }

        try:
            token_response = requests.post(provider_config['token_url'], data=token_data, headers={'Accept': 'application/json'})
            token_response.raise_for_status()
            response_data = token_response.json()
            access_token = response_data.get('access_token')
            print("Access token response:", response_data)
        except requests.exceptions.RequestException as e:
            return Response({"error": f"Failed to obtain access token: {e}"}, status=status.HTTP_400_BAD_REQUEST)

        if not access_token:
            return Response({"error": "Access token not provided by the provider"}, status=status.HTTP_400_BAD_REQUEST)

        headers = {
            'Authorization': f"Bearer {access_token}"
        }
        if provider == 'twitch':
            headers['Client-Id'] = provider_config['client_id']  # Required for Twitch

        # Fetch user data and handle each provider separately
        try:
            data_response = requests.get(provider_config['data_url'], headers=headers)
            data_response.raise_for_status()
            user_data = data_response.json()
            print("User data response:", user_data)
            
            if provider == 'twitch':
                # For Twitch, extract 'login' and 'id' from nested data
                provider_username = user_data.get('data', [{}])[0].get('login')
                provider_id = user_data.get('data', [{}])[0].get('id')
            elif provider == 'google':
                # For Google, extract directly from flat data structure
                provider_username = user_data.get('name')
                provider_id = user_data.get('id')
                email = user_data.get('email', f"{provider_username}@example.com")
            elif provider == 'spotify':
                # For Spotify, use 'display_name' and 'id', with email directly provided
                provider_username = user_data.get('display_name')
                provider_id = user_data.get('id')
                email = user_data.get('email', f"{provider_username}@example.com")
            else:
                # Generic provider (e.g., GitHub)
                provider_username = user_data.get('login')
                provider_id = user_data.get('id')
                email = user_data.get('email', f"{provider_username}@example.com")

            if not provider_username or not provider_id:
                return Response({"error": "Required user data not provided by the provider"}, status=status.HTTP_400_BAD_REQUEST)

        except requests.exceptions.RequestException as e:
            return Response({"error": f"Failed to obtain user data: {e}"}, status=status.HTTP_400_BAD_REQUEST)

        username = provider_username or email.split('@')[0] or get_random_string(10)

        # If user is authenticated, update SocialUser
        if request.user.is_authenticated:
            user = request.user
            social_user, created = SocialUser.objects.get_or_create(
                user=user,
                provider=provider,
                provider_id=provider_id,
                defaults={'access_token': access_token, 'provider_username': username}
            )
            if not created:
                social_user.access_token = access_token
                social_user.provider_username = username
                social_user.save()
            return HttpResponseRedirect("http://localhost:3000/dashboard")

        # Save or update user info for unauthenticated user
        try:
            social_user = SocialUser.objects.get(provider=provider, provider_id=provider_id)
            user = social_user.user
            social_user.access_token = access_token
            social_user.provider_username = username
            social_user.save()
        except SocialUser.DoesNotExist:
            user = User.objects.create(username=username, email=email)
            SocialUser.objects.create(
                user=user, provider=provider, provider_id=provider_id,
                access_token=access_token, provider_username=username
            )
            PersistentToken.objects.create(user=user)

        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return HttpResponseRedirect("http://localhost:3000/dashboard")