import msal
import requests
from django.conf import settings
from django.shortcuts import redirect, render
from django.http import JsonResponse

def microsoft_login(request):
    client = msal.ConfidentialClientApplication(
        settings.MICROSOFT_CLIENT_ID,
        authority=settings.MICROSOFT_AUTHORITY,
        client_credential=settings.MICROSOFT_CLIENT_SECRET
    )
    
    auth_url = client.get_authorization_request_url(
        settings.MICROSOFT_SCOPE,
        redirect_uri=settings.MICROSOFT_REDIRECT_URI
    )
    return redirect(auth_url)

def microsoft_callback(request):
    code = request.GET.get('code')
    
    if not code:
        return JsonResponse({'error': 'No code provided'}, status=400)
    
    client = msal.ConfidentialClientApplication(
        settings.MICROSOFT_CLIENT_ID,
        authority=settings.MICROSOFT_AUTHORITY,
        client_credential=settings.MICROSOFT_CLIENT_SECRET
    )
    
    token_response = client.acquire_token_by_authorization_code(
        code,
        scopes=settings.MICROSOFT_SCOPE,
        redirect_uri=settings.MICROSOFT_REDIRECT_URI
    )
    
    if 'access_token' in token_response:
        request.session['microsoft_access_token'] = token_response['access_token']
        request.session['microsoft_refresh_token'] = token_response['refresh_token']
        
        return JsonResponse({
            'access_token': token_response['access_token'],
            'refresh_token': token_response['refresh_token'],
            'expires_in': token_response['expires_in']
        })
    else:
        return JsonResponse({'error': 'Failed to acquire access token', 'details': token_response}, status=400)

def get_user_info(request):
    access_token = request.session.get('microsoft_access_token')
    
    if not access_token:
        return JsonResponse({'error': 'User not authenticated'}, status=401)
    
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    
    graph_url = 'https://graph.microsoft.com/v1.0/me'
    response = requests.get(graph_url, headers=headers)
    
    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({'error': 'Failed to fetch user info'}, status=response.status_code)
