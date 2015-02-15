from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

CITY_CHOICES = (
    ('NIC', 'Nicosia'),
    ('LAR', 'Larnaca'),
    ('LIM', 'Limassol'),
    ('PAF', 'Paphos'),
    ('FAM', 'Famagusta'),
)

class Station(models.Model):
    name    = models.CharField(max_length=128)
    company = models.CharField(max_length=32)
    city    = models.CharField(max_length=16, choices=CITY_CHOICES, default='NIC')
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

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class PriceHistory(models.Model):
    product_id = models.ForeignKey(Product)
    station_id = models.ForeignKey(Station)
    date       = models.DateTimeField()
    price      = models.DecimalField(max_digits=5, decimal_places=4)
    slug       = models.SlugField(unique=True, editable=False)
    
    def save(self, *args, **kwargs):
        print "self: %s, Type: %s" % (self.product_id.name, type(self.product_id.name))
        slug_text = str(self.product_id.name) + self.date.strftime('%d%m%Y')
        self.slug = slugify(slug_text)
        super(PriceHistory, self).save(*args, **kwargs)   
    def __unicode__(self):
        slug_text = str(self.product_id.name) + self.date.strftime('%d%m%Y')
        return slug_text 
