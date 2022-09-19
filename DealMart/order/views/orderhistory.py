from django.shortcuts import render
from django.views.generic import ListView
from order.models import Order
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class OrderHistory(ListView):
    template_name = "order/order_history.html"

    def get(self,request):  
        total = 0
        orders = Order.objects.filter(created_by=request.user).order_by('-id')
        for i in orders:
            for j in i.cart.all():
                total = j.product.price * j.quantity + total
            i.total_amount = total
            total = 0
        return render(request,self.template_name,{'orders':orders})