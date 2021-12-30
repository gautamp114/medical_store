from product.models import Brand,Category, GenericName,Product
from django.contrib import admin

admin.site.register(Category)
admin.site.register(GenericName)
admin.site.register(Brand)
admin.site.register(Product)
