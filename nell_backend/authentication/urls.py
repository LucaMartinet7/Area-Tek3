from django.urls import path
from .views import OAuthLoginView, OAuthCallbackView  # Import both views here

urlpatterns = [
    path('oauth/login/<str:provider>/', OAuthLoginView.as_view(), name='oauth_login'),
    path('oauth/callback/', OAuthCallbackView.as_view(), name='oauth_callback'),
]
