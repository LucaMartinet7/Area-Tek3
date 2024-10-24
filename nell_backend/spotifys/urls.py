from django.urls import path, include
from .views import spotify_login, spotify_callback, get_user_playlists, check_spotify_beatles

urlpatterns = [
    path('login/', spotify_login, name='spotify_login'),
    path('callback/', spotify_callback, name='spotify_callback'),
    path('playlists/', get_user_playlists, name='get_user_playlists'),
    path('check-beatles/', check_spotify_beatles, name='check_spotify_beatles'),
]
