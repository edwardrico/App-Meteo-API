from datetime import datetime

import pytz
from django.shortcuts import render
from django.http import HttpResponse
import requests


def home_view(request):
    try:
        ville = request.GET.get('ville', 'Nantes')
        cle_api = "a9cfc5cad5f990b591cc43b343e639ba"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={ville}&appid={cle_api}"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        temperature = round(data['main']['temp'] - 273.15)
        humidity = data['main']['humidity']
        weather = data['weather'][0]['main']
        weather_description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        city = data['name']
        country = data['sys']['country']
        wind = data['wind']['speed']
        wind_direction = data['wind']['deg']

        timezone_offset = data['timezone']
        city_timezone = pytz.timezone(
            pytz.country_timezones[country][0]) if country in pytz.country_timezones else pytz.timezone('UTC')


        current_datetime = datetime.now(city_timezone)

        context = {
            'temperature': temperature,
            'humidity': humidity,
            'weather': weather,
            'weather_description': weather_description,
            'icon': icon,
            'city': city,
            'country': country,
            'wind': wind,
            'wind_direction': wind_direction,
            'current_datetime': current_datetime,
        }
        return render(request, 'home.html', context)
    except requests.exceptions.HTTPError as e:
        return HttpResponse(f"Erreur de requête : {response.status_code}")


    except Exception as e:
        return HttpResponse(f"Erreur : {e}")
