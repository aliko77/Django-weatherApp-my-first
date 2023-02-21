import requests


def fahToCel(temp):
    return round((temp - 32) * 5 / 9)


class CityWeather:
    def weather(city):
        APIKEY = 'APIKEY'
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&lang=tr&appid=' + APIKEY
        cityWeather = requests.get(url.format(city)).json()
        if cityWeather['cod'] == '404':
            return cityWeather

        cityWeather['main']['tempCel'] = fahToCel(
            cityWeather['main']['temp']
        )
        cityWeather['main']['tempCelFeel'] = fahToCel(
            cityWeather['main']['feels_like']
        )
        cityWeather['wind']['speedH'] = round(
            cityWeather['wind']['speed'] * 0.44704, 1)
        weather = {
            'weather': cityWeather['weather'][0],
            'temp': cityWeather['main'],
            'wind': cityWeather['wind'],
            'country': cityWeather['sys']['country'],
            'city': cityWeather['name']
        }
        return weather
