from django.shortcuts import redirect
from django.http import JsonResponse
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from django.conf import settings

def youtube_login(request):
    flow = Flow.from_client_config(
        {
            "web": {
                "client_id": settings.YOUTUBE_CLIENT_ID,
                "client_secret": settings.YOUTUBE_CLIENT_SECRET,
                "redirect_uris": [settings.YOUTUBE_REDIRECT_URI],
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
            }
        },
        scopes=settings.YOUTUBE_SCOPES
    )
    
    authorization_url, state = flow.authorization_url(access_type='offline')
    request.session['state'] = state
    return redirect(authorization_url)

def youtube_callback(request):
    flow = Flow.from_client_config(
        {
            "web": {
                "client_id": settings.YOUTUBE_CLIENT_ID,
                "client_secret": settings.YOUTUBE_CLIENT_SECRET,
                "redirect_uris": [settings.YOUTUBE_REDIRECT_URI],
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
            }
        },
        scopes=settings.YOUTUBE_SCOPES
    )
    
    flow.fetch_token(authorization_response=request.build_absolute_uri())
    credentials = flow.credentials

    request.session['youtube_credentials'] = credentials_to_dict(credentials)

    return JsonResponse({'status': 'success', 'credentials': credentials_to_dict(credentials)})

def credentials_to_dict(credentials):
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }

def get_youtube_channels(request):
    credentials = request.session.get('youtube_credentials')
    if not credentials:
        return JsonResponse({'error': 'User not authenticated'}, status=401)

    youtube = build('youtube', 'v3', credentials=credentials)
    request = youtube.channels().list(part='snippet,contentDetails', mine=True)
    response = request.execute()
    
    return JsonResponse(response)
