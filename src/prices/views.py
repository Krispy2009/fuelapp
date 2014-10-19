from django.shortcuts import render
from django.http import HttpResponse
from .models import Station

# Create your views here.


def index(request):
    stations = Station.objects.all()
    ctx = {
        'boldmessage' : 'This is bold message',
        'stations'    : stations
    }
    return render(request, 'prices/index.html', ctx)

def aboutus(request):
    ctx = {'boldmessage' : 'Hey ya'}
    return render(request, 'prices/about.html', ctx)