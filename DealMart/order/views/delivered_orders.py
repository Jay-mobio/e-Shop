from django.contrib.auth.decorators import login_required
from product_admin.mixins import CheckProductOwnerGroup
from django.utils.decorators import method_decorator
from django.views.generic import ListView,View
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from customer.models import Cart
from order.models import Order

@method_decorator(login_required, name='dispatch')
class DeliveredOrder(CheckProductOwnerGroup,ListView):
    template_name = "order/order_delivered.html"
    paginate_by = 10
    
    def get(self,request):
        orders = Order.objects.filter(status = 'delivered').order_by('-id').only('id','cart','total_amount','address','first_name','last_name','phone','status','created_at')
        cart = Cart.objects.filter(created_by = request.user,is_active=True).count()
        current_ordres = []
        total = 0

        for i in orders:
            for j in i.cart.all():
                if j.product.created_by == request.user: total = j.product.price * j.quantity + total

            i.total_amount = total

            if total > 0: current_ordres.append(total)

            total = 0 

        paginator  = Paginator(current_ordres,self.paginate_by)
        page_number = request.GET.get('page',1)
        current_ordres = paginator.get_page(page_number)
        context = {'orders':orders,'page_number':page_number, 'order_status':[i for i,j  in Order.STATUS],'cart':cart,'current_ordres':current_ordres}

        return render(request,self.template_name,context)

class OrderStatusUpdate(View):

    def get(self,request,pk):
        order = Order.objects.get(id=pk)
        order.status = request.GET.get('status')
        order.save()

        return redirect("order:current_order")
