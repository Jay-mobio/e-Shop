from django.shortcuts import render,redirect
from order.models import Order
from django.views.generic import ListView,View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from product_admin.mixins import CheckProductOwnerGroup
from customer.models import Cart
from products.models import Category
from django.core.paginator import Paginator

@method_decorator(login_required, name='dispatch')
class CurrentOrders(CheckProductOwnerGroup,ListView):
    template_name = "order/current_orders.html"
    paginate_by = 10
    
    def get(self,request):
        orders = Order.objects.filter(status__in = ('pending','out for delivery')).order_by('-id')
        cart = Cart.objects.filter(created_by = request.user,is_active=True)
        category = Category.objects.all()
        current_ordres = []
        total = 0
        for i in orders:
            for j in i.cart.all():
                if j.product.created_by == request.user:
                    total = j.product.price * j.quantity + total
            i.total_amount = total
            if total > 0:
                current_ordres.append(total)
            total = 0 
        paginator  = Paginator(orders,self.paginate_by)
        page_number = request.GET.get('page',1)
        orders = paginator.get_page(page_number)
        context = {'orders':orders,'page_number':page_number, 'order_status':[i for i,j  in Order.STATUS],'cart':cart,'current_ordres':current_ordres,'category':category}
        return render(request,self.template_name,context)

class OrderStatusUpdate(View):

    def get(self,request,pk):
        order = Order.objects.get(id=pk)
        order.status = request.GET.get('status')
        order.save()
        return redirect("order:current_order")
