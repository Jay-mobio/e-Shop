from django.shortcuts import render,redirect
from order.models import Order
from django.views.generic import TemplateView,View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from product_admin.mixins import CheckProductOwnerGroup
from customer.models import Cart

@method_decorator(login_required, name='dispatch')
class CurrentOrders(CheckProductOwnerGroup,TemplateView):
    template_name = "order/current_orders.html"

    def get(self,request):
        orders = Order.objects.filter(status__in = ('pending','out for delivery')).order_by('-id')
        cart = Cart.objects.filter(created_by = request.user,is_active=True)    
        context = {'orders':orders, 'order_status':[i for i,j  in Order.STATUS],'cart':cart}
        return render(request,self.template_name,context)

class OrderStatusUpdate(View):

    def get(self,request,pk):
        order = Order.objects.get(id=pk)
        order.status = request.GET.get('status')
        order.save()
        return redirect("order:current_order")
