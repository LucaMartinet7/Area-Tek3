from django.urls import path, include
from rest_framework.routers import DefaultRouter
from integrations.views import ServiceViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
