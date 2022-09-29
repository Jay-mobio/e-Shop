"""CREATE ORDER VIEW"""
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.template.loader import get_template
from django.views.generic import TemplateView
from django.shortcuts import redirect,render
from django.core.mail import EmailMessage
from django.conf import settings
from customer.models import Cart
from order.models import Order

class CreateOrder(CreateView):
    """OPERATION FOR CREATE ORDER"""
    def post(self, request):
        """CREATE ORDER OPERATION"""
        cart = Cart.objects.filter(created_by = request.user,is_active=True).only
        ('id','product__price','quantity')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        order = Order.objects.create(created_by=request.user,first_name=first_name,
                last_name=last_name,phone=phone,address=address)
        total = self.get_total(cart,order)
        user = request.user
        order.total_amount = total
        order.save()

        context = {'cart':cart,'total':total}
        self.send_mail(self,context,user)
        cart.update(is_active=False)

        return redirect("order:order_placed")

    def get_total(self,cart):
        """GET TOTAL FOR ORDER"""
        total = 0
        for i in cart: total = i.product.price * i.quantity + total
        return total

    def send_mail(self,context,user):
        """SEND MAIL AFTER ORDER TO THE USER"""
        message = get_template('order/order_email.html').render(context)
        msg = EmailMessage(
        'Order recieved',
        message,
        settings.EMAIL_HOST_USER,
        [user],
        )
        msg.content_subtype ="html"
        msg.send()

@method_decorator(login_required, name='dispatch')
class OrderPlaced(TemplateView):
    """ORDER PLACED PAGE DISPLAY"""
    template_name = "order/orderplaced.html"
    def get(self,request):
        """ORDER IS PALCED MESSAGE"""
        return render(request,self.template_name)
