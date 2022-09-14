from django.shortcuts import render
from django.views.generic import ListView
from customer.models import Cart
from user_module.models import User

class Checkout(ListView):
    template_name = "order/checkout.html"

    def get(self,request):
        cart = Cart.objects.filter(created_by = request.user,is_active=True)
        total = 0
        for i in cart:
            total = i.product.price * i.quantity + total
        return render(request,self.template_name,{'cart':cart,'total':total})

