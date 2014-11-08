from django import template
from prices.models import Station

register = template.Library()

@register.inclusion_tag('prices/cities.html')
def get_stations_list(city=None):
    print 'HEEEE'
    print city, Station.objects.filter(city=city) 
    return {'stations': Station.objects.filter(city=city), 'curr_city' : city}