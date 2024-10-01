from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from allauth.socialaccount.providers.google.views import oauth2_login as google_login_view
from allauth.socialaccount.providers.github.views import oauth2_login as github_login_view
from allauth.socialaccount.providers.discord.views import oauth2_login as discord_login_view
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    @swagger_auto_schema(request_body=RegisterSerializer)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)

# Social login views wrapped for Swagger
@swagger_auto_schema(method='get', operation_description="Login with Google OAuth2")
@api_view(['GET'])
def google_login(request):
    return google_login_view(request)

@swagger_auto_schema(method='get', operation_description="Login with GitHub OAuth2")
@api_view(['GET'])
def github_login(request):
    return github_login_view(request)

@swagger_auto_schema(method='get', operation_description="Login with Discord OAuth2")
@api_view(['GET'])
def discord_login(request):
    return discord_login_view(request)
