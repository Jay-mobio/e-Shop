from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render,redirect
from django.views.generic import ListView
from order.mixins import CheckCart
from customer.models import Cart


@method_decorator(login_required, name='dispatch')
class Checkout(CheckCart,ListView):
    template_name = "order/checkout.html"

    def get(self,request):
        cart = Cart.objects.filter(created_by = request.user,is_active=True).only('product__name','product__price','product_total','quantity')
        total =  self.get_total_amount(cart)
        context = {'cart':cart,'total':total}
        return render(request,self.template_name,context)
    
    def get_total_amount(self,cart):
        total = 0
        total_amount = [total + i.product.price * i.quantity for i in cart]
        return total_amount[0]

