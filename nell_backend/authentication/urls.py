from django.urls import path, include
from .views import RegisterView, google_login, github_login, discord_login
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),

    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    # Social login URLs
    path('dj-rest-auth/google/login/', google_login, name='google_login'),
    path('dj-rest-auth/github/login/', github_login, name='github_login'),
    path('dj-rest-auth/discord/login/', discord_login, name='discord_login'),

    # Allauth Social login URLs
    path('accounts/', include('allauth.urls')),
]
