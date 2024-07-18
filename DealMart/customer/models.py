"""CUSTOMER MODELS"""
from django.db import models
from products.models import SubCategory
from products.models import Inventory,Products
from user_module.models import User

# Create your models here.

class Cart(models.Model):
    """CART MODELS"""
    inventory = models.ForeignKey(Inventory,on_delete=models.CASCADE, related_name="inventory",null=True)
    product = models.ForeignKey(Products,on_delete=models.CASCADE, related_name="products",null=True)
    size = models.ForeignKey(SubCategory,on_delete=models.CASCADE,related_name="suze",null=True)
    quantity = models.IntegerField(default=1,null=True,blank=True)
    product_total = models.BigIntegerField(default=1,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now_add = True, null = True)
    created_by = models.ForeignKey (User,on_delete=models.CASCADE, related_name="created_cart",null=True)
    updated_by = models.ForeignKey (User,on_delete=models.CASCADE,related_name="updated_cart" ,null=True)
