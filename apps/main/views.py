from django.shortcuts import render
from django.views import View
from .functions.location import Location
from .functions.cityWeather import CityWeather

# Create your views here.


class index(View):
    async def get(self, request):
        location = Location.getUserLocation()
        city_weather = CityWeather.weather(location)

        context = {
            'location': location,
            'weather': city_weather
        }

        return render(
            request=request,
            template_name='index.html',
            context=context
        )
