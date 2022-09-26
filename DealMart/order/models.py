from tkinter import N
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

    cart = models.ManyToManyField(Cart)
    total_amount = models.IntegerField(null=True,blank=True)
    status = models.CharField(max_length=200,null = True,choices=STATUS,blank=True,default='pending')
    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255,null=True,blank=True)
    phone = models.CharField(max_length=10, blank=True)
    address = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now_add = True, null = True)
    created_by = models.ForeignKey (User,on_delete=models.CASCADE, related_name="created_order",null=True)
    updated_by = models.ForeignKey (User,on_delete=models.CASCADE,related_name="updated_order" ,null=True)

    def __str__(self):
        return str(self.created_by)

