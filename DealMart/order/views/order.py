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
    def post(self, request):
        cart = Cart.objects.filter(created_by = request.user,is_active=True).only('id','product__price','quantity')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        order = Order.objects.create(created_by=request.user,first_name=first_name,last_name=last_name,phone=phone,address=address)

        total = self.get_total(cart,order)        
        user = request.user
        
        context = {'cart':cart,'total':total}
        self.send_mail(self,context,user)
        cart.update(is_active=False)      

        return redirect("order:order_placed")

    def get_total(self,cart,order):
        total = 0
        for i in cart:
            total = i.product.price * i.quantity + total
        return total
    
    def send_mail(self,request,context,user):
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
    template_name = "order/orderplaced.html"
    def get(self,request):
        cart = Cart.objects.filter(created_by = request.user,is_active=True).only('id')
        return render(request,self.template_name,{'cart':cart})
