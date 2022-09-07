from django.shortcuts import render
from django.views.generic import ListView
from customer.models import Cart
from user_module.models import User

class Checkout(ListView):
    template_name = "order/checkout.html"

    def get(self,request):
        cart = Cart.objects.all()
        user = request.user
        user = User.objects.filter(email=user)

        return render(request,self.template_name,{'cart':cart})

