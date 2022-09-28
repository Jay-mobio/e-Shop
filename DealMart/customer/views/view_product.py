"""VIEW PRODUCT"""
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render,redirect
from django.views.generic import DetailView
from django.contrib import messages
from products.models import SubCategory
from products.models import Products
from customer.models import Cart

@method_decorator(login_required, name='dispatch')
class ProductView(DetailView):
    """VIEW PRODUCT DETAILS"""
    template_name = "customer/product_view.html"

    def get(self,request,pk):
        """GETTING PRODUCT DETAILS"""
        product = Products.objects.get(pk=pk)
        cart = Cart.objects.filter(is_active=True,created_by = request.user).only('id')
        sub_categorys = SubCategory.objects.filter(category = product.category).only('id','name')

        context = {
            'product':product,
            'sub_categorys':sub_categorys,
            'cart':cart,
        }

        return render(request,self.template_name,context)

    def post(self,request,pk):
        """ADDING PRODUCT TO CART"""
        product = Products.objects.get(pk=pk)
        quantity = int(request.POST.get('quantity'))
        sub_category = request.POST.get('sub_category')

        if Cart.objects.filter(product=product,is_active=True,created_by=request.user,size_id=sub_category).exists():
            cart = Cart.objects.filter(product=product,is_active=True,created_by=request.user,size_id=sub_category)
            quantityy = cart[0].quantity + quantity
            product_total = quantityy * product.price
            cart.update(product=product,is_active=True,created_by=request.user,quantity=quantityy,size_id=sub_category,product_total=product_total)
            messages.success(request,"Quantity increased in cart")
            return redirect(request.path_info)

        product_total = quantity * product.price
        cart = Cart.objects.create(product=product,created_by=request.user,quantity=quantity,product_total=product_total,size_id=sub_category)
        cart.sub_category = sub_category
        cart.save()

        messages.success(request,"Product Has Been Added To Cart")
        return redirect(request.path_info)
