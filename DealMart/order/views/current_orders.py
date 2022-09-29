"""ORDER RECIEVED FOR PRODUCT ADMIN"""
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView,View
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from products.models import Category
from customer.models import Cart
from order.models import Order
from product_admin.mixins import CheckProductOwnerGroup

@method_decorator(login_required, name='dispatch')
class CurrentOrders(CheckProductOwnerGroup,ListView):
    """LIST OF RICEVED ORDERS"""
    template_name = "order/current_orders.html"
    paginate_by = 10

    def get(self,request):
        """GET DETAILS OF RECIEVED ORDERS BY PRODUCT ADMIN"""
        search = request.GET.get('search', "")
        ordering = request.GET.get('ordering',"")
        orders = Order.objects.filter(status__in = ('pending','out for delivery')).order_by('-id')\
        .only('id','status','created_by',
        'created_by__first_name','created_by__last_name','created_by__profile_pic',
        'created_at','cart__product__price','cart__quantity')
        cart = Cart.objects.filter(created_by = request.user,is_active=True).count()
        category = Category.objects.all().only('id','name')
        current_orders = []
        user = request.user
        self.get_current_orders(orders,current_orders,user)

        orders = self.get_queryset(ordering,search,orders)


        paginator  = Paginator(orders,self.paginate_by)
        page_number = request.GET.get('page',1)
        orders = paginator.get_page(page_number)
        context = {'orders':orders,'page_number':page_number,
            'order_status':[i for i,j  in Order.STATUS],'cart':cart,
            'current_orders':current_orders,'category':category}
        return render(request,self.template_name,context)

    def get_queryset(self,ordering,search,orders):
        """GET QUERYSET FOR FILTER AND ORDERING"""
        sort = {
            "low_to_high":'product__price',
            "high_to_low":'-product__price'
        }

        ordering =  sort[ordering] if ordering in sort else None

        if ordering is not None:
            orders = orders.order_by(ordering)
        else:
            pass

        if search != "":
            orders = orders.filter(created_by__email__in = search)
        else:
            pass

        return orders

    def get_current_orders(self,orders,current_orders,user):
        """GETTING CURRENT ORDERS FOR PAGINATION"""
        total = 0
        for i in orders:
            # total = [j.product.price * j.quantity + total for j in i.cart.all()
            # if j.product.created_by == request.user]
            for j in i.cart.all():

                if j.product.created_by == user:
                    total = j.product.price * j.quantity + total

                i.total_amount = total
                if i.total_amount > 0:
                    current_orders.append(i.total_amount)

                total = 0
        return current_orders

class OrderStatusUpdate(View):
    """UPDATE ORDER STATUS"""
    def get(self,request,pk):
        """GETTING ORDER STATUS AND UPDATE"""
        order = Order.objects.get(id=pk)
        order.status = request.GET.get('status')
        order.save()
        return redirect("order:current_order")
