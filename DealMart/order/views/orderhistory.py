from django.shortcuts import render
from django.views.generic import ListView
from order.models import Order

class OrderHistory(ListView):
    template_name = "order/order_history.html"

    def get(self,request):
        orders = Order.objects.filter(created_by=request.user)
        return render(request,self.template_name,{'orders':orders})