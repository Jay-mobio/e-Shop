from django.contrib import admin
from products.models import Products,Category,Inventory,SubCategory
# Register your models here.
admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Inventory)
admin.site.register(SubCategory)