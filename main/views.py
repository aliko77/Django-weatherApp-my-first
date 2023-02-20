from django.shortcuts import render
from django.views import View
from .functions.location import Location
import requests

# Create your views here.


class index(View):
    async def get(self, request):
        location = Location.getUserLocation()
        APIKEY = '7c8796e389e4f40e0e76f0079d4b51a7'
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=7c8796e389e4f40e0e76f0079d4b51a7'
        city = location
        city_weather = requests.get(url.format(city)).json()

        context = {
            'location': location,
            'temperature': city_weather
        }
        return render(
            request=request,
            template_name='index.html',
            context=context
        )
