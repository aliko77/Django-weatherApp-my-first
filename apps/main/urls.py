from django.urls import path
from apps.main.views import index, weather

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('weather', weather.as_view(), name='weather')
]
