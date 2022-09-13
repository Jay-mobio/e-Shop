from ast import Or
from django.shortcuts import render,redirect
from order.models import Order
from django.views.generic import TemplateView,View
class CurrentOrders(TemplateView):
    template_name = "order/current_orders.html"

    def get(self,request):
        orders = Order.objects.filter(status__in = ('pending','out for delivery'))  
        return render(request,self.template_name,{'orders':orders, 'order_status':[i for i,j  in Order.STATUS]})

class OrderStatusUpdate(View):

    def get(self,request,pk):
        order = Order.objects.get(id=pk)
        order.status = request.GET.get('status')
        order.save()
        return redirect("order:current_order")
