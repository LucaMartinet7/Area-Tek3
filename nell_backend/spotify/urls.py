from django.urls import path, include
from .views import spotify_login, spotify_callback, get_user_playlists

urlpatterns = [
    path('login/', spotify_login, name='spotify_login'), #edit le path car 2 fois spotify dedans
    path('callback/', spotify_callback, name='spotify_callback'),
    path('playlists/', get_user_playlists, name='get_user_playlists'),
]
