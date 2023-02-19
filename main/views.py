from django.shortcuts import render
from django.views import View
from .functions.location import Location

# Create your views here.


class index(View):
    def get(self, request):
        context = {
            'location': Location.getUserLocation()
        }
        return render(
            request=request,
            template_name='index.html',
            context=context
        )
