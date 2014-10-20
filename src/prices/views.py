from django.shortcuts import render
from django.http import HttpResponse

from .models import Station, Product
from fuelapp.forms import StationForm

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
    
def add_station(request):
    if request.method == 'POST':
        form = StationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = StationForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'prices/add_station.html', {'form': form})