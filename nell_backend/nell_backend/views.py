import requests
from django.http import JsonResponse
from django.conf import settings

def get_spotify_token():
    auth_url = "https://accounts.spotify.com/api/token"
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': settings.SPOTIFY_CLIENT_ID,
        'client_secret': settings.SPOTIFY_CLIENT_SECRET,
    })
    auth_data = auth_response.json()
    return auth_data['access_token']

def spotify_search(request):
    token = get_spotify_token()
    search_query = request.GET.get('q', 'Coldplay')
    headers = {
        'Authorization': f'Bearer {token}',
    }
    params = {
        'q': search_query,
        'type': 'artist',
        'limit': 10,
    }
    search_url = "https://api.spotify.com/v1/search"
    response = requests.get(search_url, headers=headers, params=params)
    
    return JsonResponse(response.json())

#Some requests can be done in front-end like that (port needs to be changed)
# http://localhost:8000/spotify/search/?q=Beatles

def get_weather_by_city(request):
    city = request.GET.get('city', 'London')  # Set to London but can do other cities
    api_key = settings.OPENWEATHER_API_KEY
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(weather_url)
    
    if response.status_code == 200:
        data = response.json()
        return JsonResponse({
            'city': data['name'],
            'temperature': data['main']['temp'],
            'weather': data['weather'][0]['description'],
            'wind_speed': data['wind']['speed'],
        })
    else:
        return JsonResponse({'error': 'City not found or API request failed.'}, status=response.status_code)

#Some requests can be done in front-end like that (port needs to be changed)  
# http://localhost:8000/weather/?city=Paris
