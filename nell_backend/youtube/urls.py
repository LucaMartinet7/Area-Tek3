from django.urls import path
from .views import youtube_login, youtube_callback, get_youtube_channels

urlpatterns = [
    path('login/', youtube_login, name='youtube_login'),
    path('callback/', youtube_callback, name='youtube_callback'),
    path('channels/', get_youtube_channels, name='get_youtube_channels'),
]
