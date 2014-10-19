from django.contrib import admin
from .models import Station, Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('station_id', 'name', 'price')
    prepopulated_fields = {'slug': ('name',)}
    
admin.site.register(Station)
admin.site.register(Product, ProductAdmin)


