from django.db import models
from products.models import Inventory
from user_module.models import User

# Create your models here.

class Cart(models.Model):
    inventory = models.ForeignKey(Inventory,on_delete=models.CASCADE, related_name="inventory",null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now_add = True, null = True)
    created_by = models.ForeignKey (User,on_delete=models.CASCADE, related_name="created_cart",null=True)
    updated_by = models.ForeignKey (User,on_delete=models.CASCADE,related_name="updated_cart" ,null=True)