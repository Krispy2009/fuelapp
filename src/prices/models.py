from django.db import models

# Create your models here.

class Station(models.Model):
    name    = models.CharField(max_length=128)
    company = models.CharField(max_length=32)
    city    = models.CharField(max_length=16)


class Product(models.Model):
    station_id = models.ForeignKey(Station)
    name       = models.CharField(max_length=64)
    price      = models.DecimalField(max_digits=5, decimal_places=4)


class PriceHistory(models.Model):
    product_id = models.ForeignKey(Product)
    date       = models.DateTimeField(auto_now_add=True)
    price      = models.DecimalField(max_digits=5, decimal_places=4)
