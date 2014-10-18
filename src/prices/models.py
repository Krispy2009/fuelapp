from django.db import models

# Create your models here.

class Station(models.Model):
    name    = models.CharField(max_length=128)
    date    = models.DateTimeField(auto_now_add=True)
    price   = models.DecimalField(max_digits=5, decimal_places=4)
    company = models.CharField(max_length=32)
    city    = models.CharField(max_length=16)

class PriceHistory(models.Model):
    station_id = models.ForeignKey(Station)
    date       = models.DateTimeField(auto_now_add=True)
    price      = models.DecimalField(max_digits=5, decimal_places=4)

