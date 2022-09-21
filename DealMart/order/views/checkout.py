from django.shortcuts import render,redirect
from django.views.generic import ListView
from customer.models import Cart
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from order.mixins import CheckCart


@method_decorator(login_required, name='dispatch')
class Checkout(CheckCart,ListView):
    template_name = "order/checkout.html"

    def get(self,request):
        cart = Cart.objects.filter(created_by = request.user,is_active=True)
        total = 0
        for i in cart:
            total = i.product.price * i.quantity + total
        context = {'cart':cart,'total':total}
        return render(request,self.template_name,context)

