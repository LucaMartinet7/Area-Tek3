from django.urls import path, include
from .views import spotify_search

urlpatterns = [
    path('spotify/search/', spotify_search, name='spotify_search'),
]
