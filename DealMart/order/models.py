from ast import Delete
from tkinter import CASCADE
from django.db import models
from customer.models import Cart
from user_module.models import User
# Create your models here.
class Order(models.Model):

    STATUS = (
        ('pending','pending'),
        ('out for delivery','out for delivery'),
        ('delivered','delivered'),
    )

    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,null=True)
    total_amount = models.IntegerField(null=True,blank=True)
    status = models.CharField(max_length=200,null = True,choices=STATUS)
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now_add = True, null = True)
    created_by = models.ForeignKey (User,on_delete=models.CASCADE, related_name="created_order",null=True)
    updated_by = models.ForeignKey (User,on_delete=models.CASCADE,related_name="updated_order" ,null=True)