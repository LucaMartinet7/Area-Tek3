from django.urls import path, include
from .views import get_weather
from . import views

urlpatterns = [
    path('weather/', views.get_weather, name='get_weather'),
]