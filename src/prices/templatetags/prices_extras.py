from django import template
from prices.models import Station

register = template.Library()

@register.inclusion_tag('prices/cities.html')
def get_stations_list(city=None):
    return {'stations': Station.objects.filter(city=city), 'curr_city' : city}