from django.shortcuts import render,redirect
from django.views.generic import ListView
from customer.models import Cart
from user_module.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages


@method_decorator(login_required, name='dispatch')
class Checkout(ListView):
    template_name = "order/checkout.html"

    def get(self,request):
        cart = Cart.objects.filter(created_by = request.user,is_active=True)
        if len(cart) == 0:
            messages.warning(request,"Add items to make an order")
            return redirect("authentication:home")
        total = 0
        for i in cart:
            total = i.product.price * i.quantity + total
        return render(request,self.template_name,{'cart':cart,'total':total})

