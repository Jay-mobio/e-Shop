from django.shortcuts import redirect,render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.conf import settings
from customer.models import Cart
from order.models import Order
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.contrib import messages

class CreateOrder(CreateView):    
    def post(self, request):
        cart = Cart.objects.filter(created_by = request.user,is_active=True)
        phone = request.user.phone
        address = request.user.address
        if address=="" or phone =="":
            messages.error(request,"Address or phone is not mentioned")
            return redirect('authentication:home')
        order = Order.objects.create(created_by=request.user)
        total = 0
        for i in cart:
            total = i.product.price * i.quantity + total
            order.cart.add(i)
        

        Cart.objects.filter(created_by = request.user).update(is_active=False)
        context = {'cart':cart,'total':total,'address':address}
        message = get_template('order/order_email.html').render(context)
        msg = EmailMessage(
        'Order recieved',
        message,
        settings.EMAIL_HOST_USER,
        [request.user],
        )
        msg.content_subtype ="html"
        msg.send()

        return redirect("order:order_placed")

class OrderPlaced(TemplateView):
    template_name = "order/orderplaced.html"
    def get(self,request):
        return render(request,self.template_name)
