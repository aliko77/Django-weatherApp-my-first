import requests


def fahToCel(temp):
    return round((temp - 32) * 5 / 9, 2)


class CityWeather:
    def weather(city):
        APIKEY = '7c8796e389e4f40e0e76f0079d4b51a7'
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=' + APIKEY
        cityWeather = requests.get(url.format(city)).json()
        cityWeather['main']['tempCel'] = fahToCel(cityWeather['main']['temp'])
        return cityWeather
