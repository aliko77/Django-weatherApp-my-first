from django.shortcuts import render, redirect
from django.views import View
from .functions.location import Location
from .functions.cityWeather import CityWeather

# Create your views here.


class index(View):
    def __init__(self):
        self.location = Location.getUserLocation()
        self.city_weather = CityWeather.weather(self.location)

    def get(self, request):
        context = {
            'location': self.location,
            'weather': self.city_weather
        }

        return render(
            request=request,
            template_name='index.html',
            context=context
        )


class weather(View):
    def post(self, request):
        city_weather = CityWeather.weather(request.POST['city'])
        context = {
            'weather': city_weather
        }
        return render(
            request=request,
            template_name='weather.html',
            context=context
        )

    def get(self, request):
        return redirect(
            to='index'
        )
