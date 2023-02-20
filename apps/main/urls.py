from django.urls import path
from apps.main.views import index

urlpatterns = [
    path('', index.as_view(), name='index')
]
