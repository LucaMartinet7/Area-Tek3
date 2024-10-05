from django.urls import path, include
from .views import get_weather_by_city
from . import views

urlpatterns = [
    path('weather/', views.get_weather_by_city, name='get_weather_by_city'),
]