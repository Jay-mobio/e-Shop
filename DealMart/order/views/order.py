from django.shortcuts import redirect,render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from customer.models import Cart
from order.models import Order

class CreateOrder(CreateView):
    template_name = "order/orders.html"

    def get(self,request):
        order = Order.objects.filter(created_by=request.user)
        return render(request,self.template_name,{'orsder':order})
    
    def post(self, request):
        cart = Cart.objects.filter(created_by = request.user)
        order = Order.objects.create(created_by=request.user)
        order.cart.set(cart)
        cart.delete()
        return redirect("order:order_placed")

class OrderPlaced(TemplateView):
    template_name = "order/orderplaced.html"
    def get(self,request):
        return render(request,self.template_name)
