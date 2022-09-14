from django.shortcuts import render
from django.views.generic import ListView
from order.models import Order

class OrderHistory(ListView):
    template_name = "order/order_history.html"

    def get(self,request):  
        total = 0
        orders = Order.objects.filter(created_by=request.user)
        for i in orders:
            for j in i.cart.all():
                total = j.product.price * j.quantity + total
            i.total_amount = total
            total = 0
        return render(request,self.template_name,{'orders':orders})