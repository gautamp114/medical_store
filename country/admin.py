from country.models import Country, District, Province
from django.contrib import admin

# Register your models here.
admin.site.register(Country)
admin.site.register(Province)
admin.site.register(District)
# admin.site.register(City)