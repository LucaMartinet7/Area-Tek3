import requests
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render

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