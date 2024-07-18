"""CART LIST PAGE"""
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView,CreateView
from django.contrib import messages
from django.shortcuts import render,redirect
from products.models import SubCategory,Products
from customer.models import Cart


@method_decorator(login_required, name='dispatch')
class ListCart(ListView):
    """CART LIST"""
    template_name = "customer/cart.html"

    def get(self,request):
        """GETTING PRODUCTS IN CART"""
        cartt = Cart.objects.filter(is_active=True,created_by = request.user).only('id','product_id','product__image','product__name','product__price','quantity','product_total','size')
        total = 0
        sub_categories = []

        if len(cartt) > 0:
            total = self.get_total(cartt)
            sub_categories = self.get_sub_categories(cartt)

        context = {
            'mylist': zip(cartt, sub_categories),
            'total':total,
            'cartt':cartt
        }
        return render(request,self.template_name,context)

    def get_total(self,cartt):
        """GETTING TOTAL OF CART PRODUCTS"""
        total = 0
        for i in cartt:
            total = i.product.price * i.quantity + total
        return total

    def get_sub_categories(self,cartt):
        """GETTING SIZE FOR CART PRODUCTS"""
        sub_categories = [SubCategory.objects.filter(category = i.product.category).only('id','name') for i in cartt]
        return sub_categories

class AddToCart(CreateView):
    model = Cart
    fields = "__all__"
    template_name = 'authentication/home.html'
    def post(self,request,pk):
        """ADDING PRODUCT TO CART"""
        product = Products.objects.get(pk=pk)
        quantity = int(request.POST.get('quantity'))
        sub_category = request.POST.get('sub_category')
        cart = Cart.objects.filter(product=product,is_active=True,created_by=request.user,size_id=sub_category)

        if cart:
            quantityy = cart[0].quantity + quantity
            product_total = quantityy * product.price
            cart.update(product=product,is_active=True,created_by=request.user,quantity=quantityy,size_id=sub_category,product_total=product_total)
            messages.success(request,"Quantity increased in cart")
            return redirect("customer:product_view" ,pk)

        product_total = quantity * product.price
        cart = Cart.objects.create(product=product,created_by=request.user,quantity=quantity,product_total=product_total,size_id=sub_category)
        cart.sub_category = sub_category
        cart.save()

        messages.success(request,"Product Has Been Added To Cart")
        return redirect("customer:product_view",pk)

