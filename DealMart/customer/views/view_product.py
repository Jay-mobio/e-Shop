"""VIEW PRODUCT PAGE"""
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
        cart = Cart.objects.filter(is_active=True,created_by = request.user).count()
        print(cart) 
        sub_categorys = SubCategory.objects.filter(category = product.category).only('id','name')

        context = {
            'product':product,
            'sub_categorys':sub_categorys,
            'cart':cart,
        }

        return render(request,self.template_name,context)
