from django.shortcuts import render
from django.http import HttpResponse
from .models import Station, Product

# Create your views here.


def index(request):
    stations = Station.objects.all()
    products = Product.objects.all().order_by('price')
    cheapest_station = products[0].station_id
    ctx = {
        'boldmessage'      : 'This is bold message',
        'stations'         : stations,
        'cheapest_station' : cheapest_station
    }
    return render(request, 'prices/index.html', ctx)

def aboutus(request):
    ctx = {'boldmessage' : 'Hey ya'}
    return render(request, 'prices/about.html', ctx)
    
def station(request, station_name_slug):
    ctx = {}
    
    try:
        # Create a Station object using the station_name_slug
        station = Station.objects.get(slug=station_name_slug)
        
        products = Product.objects.filter(station_id=station)
        
        ctx.update({
            'products': products,
            'station' : station
        })
    except Station.DoesNotExist:
        pass
    
    return render(request, 'prices/station.html', ctx)