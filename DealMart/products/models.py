from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    
    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(max_length=18)
    image = models.ImageField(null=True, blank=True)
    discription = models.TextField
    date_created = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return self.label

class Inventory(models.Model):
    product_quantity = models.IntegerField(max_length=200)
    is_active = models.BooleanField(default=False)