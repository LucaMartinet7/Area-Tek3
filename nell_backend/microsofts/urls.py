from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OutlookReactionViewSet, TriggerOutlookEmailAPIView, microsoft_callback, microsoft_login, get_user_info

router = DefaultRouter()
router.register(r'reactions', OutlookReactionViewSet)

urlpatterns = [
    path('trigger-email/', TriggerOutlookEmailAPIView.as_view(), name='trigger_outlook_email'),
    path('login/', microsoft_login, name='microsoft_login'),
    path('callback/', microsoft_callback, name='microsoft_callback'),
    path('me/', get_user_info, name='get_user_info'),
    path('', include(router.urls)),
]
