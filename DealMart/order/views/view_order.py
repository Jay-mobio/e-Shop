from django.shortcuts import render,redirect
from django.views.generic.edit import UpdateView
from order.models import Order

class ViewOrder(UpdateView):
    template_name = "order/view_order.html"

    def get(self,request,pk):
        order = Order.objects.get(id=pk)   
        total = 0

        for i in order.cart.all():
            if i.product.created_by == request.user:
                    total = i.product.price * i.quantity + total
            total_amount = total

        context = {'order':order,'total_amount':total_amount,'order_status':[i for i,j  in Order.STATUS]}

        return render(request,self.template_name,context)