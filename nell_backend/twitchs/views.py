import requests
from django.shortcuts import redirect
from django.http import JsonResponse
from django.conf import settings

def twitch_login(request):
    twitch_auth_url = "https://id.twitch.tv/oauth2/authorize"
    params = {
        'client_id': settings.TWITCH_CLIENT_ID,
        'redirect_uri': settings.TWITCH_REDIRECT_URI,
        'response_type': 'code',
        'scope': settings.TWITCH_SCOPES
    }

    auth_url = f"{twitch_auth_url}?" + "&".join([f"{key}={value}" for key, value in params.items()])
    return redirect(auth_url)

def twitch_callback(request):
    code = request.GET.get('code')
    if not code:
        return JsonResponse({'error': 'Missing code parameter'}, status=400)

    token_url = "https://id.twitch.tv/oauth2/token"
    data = {
        'client_id': settings.TWITCH_CLIENT_ID,
        'client_secret': settings.TWITCH_CLIENT_SECRET,
        'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': settings.TWITCH_REDIRECT_URI
    }

    response = requests.post(token_url, data=data)
    token_info = response.json()

    if 'access_token' in token_info:
        request.session['twitch_access_token'] = token_info['access_token']
        return JsonResponse({'status': 'success', 'token_info': token_info})
    else:
        return JsonResponse({'error': 'Failed to retrieve access token'}, status=400)

def get_twitch_user(request):
    access_token = request.session.get('twitch_access_token')
    if not access_token:
        return JsonResponse({'error': 'User not authenticated'}, status=401)

    user_url = "https://api.twitch.tv/helix/users"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Client-ID': settings.TWITCH_CLIENT_ID
    }

    response = requests.get(user_url, headers=headers)
    user_info = response.json()

    return JsonResponse(user_info)
