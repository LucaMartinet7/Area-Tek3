from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # JWT Login (obtain token)
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # JWT Token Refresh
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
