import re
from django.db import models
from user_module.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    date_at = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now_add = True, null = True)
    created_by = models.ForeignKey (User,on_delete=models.CASCADE, related_name="created_category")
    updated_by = models.ForeignKey (User,on_delete=models.CASCADE, related_name="updated_category")
    
    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=255)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True, default="deault.jpg")
    discription = models.TextField
    date_at = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now_add = True, null = True)
    created_by = models.ForeignKey (User,on_delete=models.CASCADE, related_name="created_product")
    updated_by = models.ForeignKey (User,on_delete=models.CASCADE,related_name="updated_product")

    def __str__(self):
        return self.label

class Inventory(models.Model):
    product_id = models.OneToOneField(Products,on_delete=models.CASCADE,primary_key=True)
    product_quantity = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    date_at = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now_add = True, null = True)
    created_by = models.ForeignKey (User,on_delete=models.CASCADE, related_name="created_inventory")
    updated_by = models.ForeignKey (User,on_delete=models.CASCADE, related_name="updated_inventory")