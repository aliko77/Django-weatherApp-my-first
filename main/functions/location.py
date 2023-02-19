from django.contrib.gis.geoip2 import GeoIP2
import socket


def get_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)


class Location:
    def getUserLocation():
        try:
            location = GeoIP2().city(get_ip())
            return location.get('city')
        except:
            return 'İstanbul'
