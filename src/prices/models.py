from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Station(models.Model):
    name    = models.CharField(max_length=128)
    company = models.CharField(max_length=32)
    city    = models.CharField(max_length=16)
    slug    = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Station, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.name


class Product(models.Model):
    station_id = models.ForeignKey(Station)
    name       = models.CharField(max_length=64)
    price      = models.DecimalField(max_digits=5, decimal_places=4)
    date       = models.DateTimeField(auto_now_add=True)
    slug       = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)   
    def __unicode__(self):
        return self.name


class PriceHistory(models.Model):
    product_id = models.ForeignKey(Product)
    date       = models.DateTimeField(auto_now_add=True)
    price      = models.DecimalField(max_digits=5, decimal_places=4)
    
    def __unicode__(self):
        return self.product_id