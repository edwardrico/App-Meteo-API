from django import forms
from django.shortcuts import render
from django.http import HttpResponse
import requests


class VilleForm(forms.Form):
    ville = forms.CharField(label='Ville', max_length=100, required=False, initial='Nantes')


def home_view(request):
    try:
        form = VilleForm(request.GET)

        if form.is_valid():
            ville = form.cleaned_data['ville']
        else:
            ville = 'Nantes'  # Valeur par défaut si le formulaire n'est pas valide

        cle_api = "a9cfc5cad5f990b591cc43b343e639ba"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={ville}&appid={cle_api}"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        # Le reste du code pour traiter les données...

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
            'form': form,  # Inclure le formulaire dans le contexte
        }
        return render(request, 'home.html', context)

    except requests.exceptions.HTTPError as e:
        return HttpResponse(f"Erreur de requête : {response.status_code}")

    except Exception as e:
        return HttpResponse(f"Erreur : {e}")
