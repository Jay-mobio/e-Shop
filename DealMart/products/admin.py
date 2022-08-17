from django.contrib import admin
from products.models import Products,Category,Inventory
# Register your models here.
admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Inventory)