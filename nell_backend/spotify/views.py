from django.shortcuts import redirect
from django.conf import settings
from django.http import JsonResponse
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def spotify_login(request):
    sp_oauth = SpotifyOAuth(
        client_id=settings.SPOTIFY_CLIENT_ID,
        client_secret=settings.SPOTIFY_CLIENT_SECRET,
        redirect_uri=settings.SPOTIFY_REDIRECT_URI,
        scope='user-read-private user-read-email playlist-read-private user-modify-playback-state'
    )
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

def spotify_callback(request):
    sp_oauth = SpotifyOAuth(
        client_id=settings.SPOTIFY_CLIENT_ID,
        client_secret=settings.SPOTIFY_CLIENT_SECRET,
        redirect_uri=settings.SPOTIFY_REDIRECT_URI
    )
    
    token_info = sp_oauth.get_access_token(request.GET.get('code'))
    
    if not token_info:
        return JsonResponse({'error': 'Failed to get access token'}, status=400)

    request.session['spotify_access_token'] = token_info['access_token']
    request.session['spotify_refresh_token'] = token_info['refresh_token']
    request.session['spotify_token_expires_in'] = token_info['expires_at']

    return JsonResponse({
        'access_token': token_info['access_token'],
        'refresh_token': token_info['refresh_token'],
        'expires_in': token_info['expires_at']
    })

def get_user_playlists(request):
    access_token = request.session.get('spotify_access_token')
    
    if not access_token:
        return JsonResponse({'error': 'User not authenticated'}, status=401)

    sp = spotipy.Spotify(auth=access_token)
    
    playlists = sp.current_user_playlists()
    
    return JsonResponse(playlists)
