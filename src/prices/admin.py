from django.contrib import admin
from .models import Station, Company, Product, UserProfile, PriceHistory

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

class CompanyAdmin(admin.ModelAdmin):
	list_display = ('name',)
	prepopulated_fields = {'slug': ('name',)}
    
admin.site.register(Station)
admin.site.register(Product, ProductAdmin)
admin.site.register(UserProfile)
admin.site.register(PriceHistory)
admin.site.register(Company)


