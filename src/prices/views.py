from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from .models import Station, Product
from fuelapp.forms import StationForm, UserForm, UserProfileForm

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

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/prices/')
            else:
                return HttpResponse('Invalid account used!')
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
            
    else:
        return render(request, 'prices/login.html', {})
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/prices')
    
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
    
    
def register(request):
    
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
            
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
        'prices/register.html',
        {
            'user_form': user_form,
            'profile_form': profile_form,
            'registered': registered
        }
    )
        
    
    
    
    
    
    