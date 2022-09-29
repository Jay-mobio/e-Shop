"""PRODUCTS MODELS"""
from django.db import models
from user_module.models import User



# Create your models here.

class Category(models.Model):
    """PRODUCT CATEGORY MODEL"""
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now_add = True, null = True)
    created_by = models.ForeignKey (User,on_delete=models.CASCADE, related_name="created_category")
    updated_by = models.ForeignKey (User,on_delete=models.CASCADE, related_name="updated_category")

    def __str__(self):
        """DISPLAY STRING"""
        return self.name


class SubCategory(models.Model):
    """PRODUCT SUBCATEGORY MODEL"""
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name="sub_category",null=True)
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now_add = True, null = True)
    created_by = models.ForeignKey (User,on_delete=models.CASCADE, related_name="created_sub_category",null=True)
    updated_by = models.ForeignKey (User,on_delete=models.CASCADE, related_name="updated_sub_category",null=True)

    def __str__(self):
        """DISPLAY STRING"""
        return self.name

class Products(models.Model):
    """PRODUCT MODEL"""
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE,null=True,blank=True)
    brand = models.CharField(max_length=255,null=True)
    price = models.IntegerField(null = True)
    image = models.ImageField(null=True, blank=True, default="static/images/default.jpg")
    discription = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now_add = True, null = True)
    created_by = models.ForeignKey (User,on_delete=models.CASCADE, related_name="created_product",null=True)
    updated_by = models.ForeignKey (User,on_delete=models.CASCADE,related_name="updated_product" ,null=True)


    def __str__(self):
        """DISPLAY STRING"""
        return self.name

class Inventory(models.Model):
    """INVENTORY MODEL"""
    product = models.OneToOneField(Products,on_delete=models.CASCADE,primary_key=True)
    product_quantity = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add = True,null = True)
    updated_at = models.DateTimeField(auto_now_add = True,null = True)
    created_by = models.ForeignKey (User,on_delete=models.CASCADE, related_name="created_inventory",null=True)
    updated_by = models.ForeignKey (User,on_delete=models.CASCADE, related_name="updated_inventory",null=True)

    def __str__(self):
        """DISPLAY STRING"""
        return self.product.name
