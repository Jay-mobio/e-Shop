from django.shortcuts import redirect,render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from customer.models import Cart
from order.models import Order

class CreateOrder(CreateView):    
    def post(self, request):
        cart = Cart.objects.filter(created_by = request.user)
        order = Order.objects.create(created_by=request.user)
        for i in cart:
            order.cart.add(i)
        Cart.objects.filter(created_by = request.user).update(is_active=False)
        return redirect("order:order_placed")

class OrderPlaced(TemplateView):
    template_name = "order/orderplaced.html"
    def get(self,request):
        return render(request,self.template_name)
