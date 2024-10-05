from django.http import JsonResponse
import requests
from django.conf import settings

def get_weather(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    
    if not lat or not lon:
        return JsonResponse({'error': 'Latitude and Longitude are required.'}, status=400)
    
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={settings.OPENWEATHER_API_KEY}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        return JsonResponse({'error': 'Failed to retrieve weather data.'}, status=response.status_code)
    
    return JsonResponse(response.json())
