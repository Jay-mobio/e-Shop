from django.shortcuts import redirect,render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.conf import settings
from customer.models import Cart
from order.models import Order

class CreateOrder(CreateView):    
    def post(self, request):
        cart = Cart.objects.filter(created_by = request.user)
        order = Order.objects.create(created_by=request.user)
        for i in cart:
            order.cart.add(i)

        Cart.objects.filter(created_by = request.user).update(is_active=False)
        mess = f"Hello {request.user.first_name},\n Thank You for ordering from DealMart\n Your order id is {order.id}"
        send_mail(
            "Welcome to DealMart",
            mess,
            settings.EMAIL_HOST_USER,
            [request.user],
            fail_silently = False
            ) 

        return redirect("order:order_placed")

class OrderPlaced(TemplateView):
    template_name = "order/orderplaced.html"
    def get(self,request):
        return render(request,self.template_name)
