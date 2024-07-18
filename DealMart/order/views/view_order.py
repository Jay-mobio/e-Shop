"""ORDER UPDATE"""
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView
from django.shortcuts import render
from order.models import Order

@method_decorator(login_required, name='dispatch')
class ViewOrder(UpdateView):
    """ORDER UPDATE AND GET OPERATIONS"""
    template_name = "order/view_order.html"

    def get(self,request,pk):
        """GETTING ORDER DETAILS"""
        order = Order.objects.get(id=pk)
        user = request.user
        total_amount = self.get_total(order,user)

        context = {'order':order,'total_amount':total_amount,
                    'order_status':[i for i,j  in Order.STATUS]}

        return render(request,self.template_name,context)

    def get_total(self,order,user):
        """GETTING TOTAL OF ORDER"""
        total = 0
        total_amount = 0
        for i in order.cart.all():
            if i.product.created_by == user: total = i.product.price * i.quantity + total
            total_amount = total + total_amount
        return total_amount
