from django import template
from prices.models import Station

register = template.Library()

@register.inclusion_tag('prices/stations.html')
def get_stations_list(station=None):
    return {'stations': Station.objects.all(), 'curr_station' : station}