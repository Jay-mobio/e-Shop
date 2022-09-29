"""ORDER HISTORY"""
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from order.models import Order
from customer.models import Cart

@method_decorator(login_required, name='dispatch')
class OrderHistory(ListView):
    """ORDER HISTORY"""
    template_name = "order/order_history.html"
    paginate_by = 10

    def get(self,request):
        """GETTING DETAILS OF USER ORDER HISTORY"""
        total = 0
        orders = Order.objects.filter(created_by=request.user).order_by('-id')
        cart = Cart.objects.filter(created_by = request.user,is_active=True).count()

        for i in orders:
            for j in i.cart.all():
                total = j.product.price * j.quantity + total
            i.total_amount = total
            total = 0

        paginator  = Paginator(orders,self.paginate_by)
        page_number = request.GET.get('page',1)
        orders = paginator.get_page(page_number)
        context = {'orders':orders,'cart':cart,'page_number':page_number}

        return render(request,self.template_name,context)
