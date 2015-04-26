from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from .models import Station, Product, HistoricalPrice
from fuelapp.forms import StationForm, UserForm, UserProfileForm

# Create your views here.


def index(request):
    stations = Station.objects.all()
    products = Product.objects.all().order_by('price')
    cheapest_station = stations[0].name
    ctx = {
        'boldmessage'      : 'This is bold message',
        'stations'         : stations,
        'cheapest_station' : cheapest_station
    }
    
    #Get Visits 
    visits = int(request.session.get('visits', 0))
    if not visits:
        visits = 0
    reset_last_visit_time = False
    
    last_visit = request.session.get('last_visit')
    if last_visit:
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
    
        if (datetime.now()-last_visit_time).days > 0:
            visits = visits + 1
            reset_last_visit_time = True
    else:
        reset_last_visit_time = True
    
    ctx['visits'] = visits
    request.session['visits'] = visits
    
    if reset_last_visit_time:
        request.session['last_visit'] = str(datetime.now())
        
    response = render(request, 'prices/index.html', ctx)
    
    return response
    
def aboutus(request):
    ctx = {'boldmessage' : 'Hey ya'}
    return render(request, 'prices/about.html', ctx)
    

def station(request, station_name_slug):
    ctx = {}
    
    try:
        # Create a Station object using the station_name_slug
        station = Station.objects.get(slug=station_name_slug)
        products = HistoricalPrice.objects.filter(station_id=station.id)        
        
        ctx.update({
            'products': products,
            'station' : station
        })
    except Station.DoesNotExist:
        pass
    
    return render(request, 'prices/station.html', ctx)

@login_required    
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

def get_city_stations(request, city):
    ctx = {}
    stations = Station.objects.filter(city=city)
    ctx.update({
        'city': city,
        'stations': stations
    })
    
    if len(stations) == 0:
        index()

def add_price(request, station_name_slug):
    return HttpResponse('Will eventually add an add price page :) ')


def all_companies(request):

    ctx = {}

    all_companies = Company.objects.all()

    return render(request, 'prices/companies.html', ctx)

def company(request, company_name_slug):
    ctx = {}

    try:
        company = Company.objects.get(slug=company_name_slug)

        ctx.update({
            'company' : company
        })
    except Company.DoesNotExist:
        pass

    return render(request, 'prices/company.html', ctx)



    
    

    
    
    
    
    
    