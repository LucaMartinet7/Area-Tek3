from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GmailReceivedActionViewSet, SetGmailTriggerView

router = DefaultRouter()
router.register(r'gmail-actions', GmailReceivedActionViewSet, basename='gmail-action')

urlpatterns = [
    path('', include(router.urls)),
    path('set-gmail-trigger/', SetGmailTriggerView.as_view(), name='set-gmail-trigger'),
]
