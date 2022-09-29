"""PRODUCT DETAILS"""
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views.generic import DetailView
from products.models import Inventory
from products.forms import AddProductForm
from customer.models import Cart

@method_decorator(login_required, name='dispatch')
class ProductDetail(DetailView):
    """PRODUCT DETAILS"""
    template_name = "products/product_detail.html"

    def get(self,request,pk):
        """GETTING PRODUCT DETAILS"""
        product = Inventory.objects.get(pk=pk)
        cart = Cart.objects.filter(created_by = request.user,is_active=True).count()
        form = AddProductForm(instance=product)
        context = {'form':form, 'product':product,'cart':cart}
        return render(request,self.template_name,context)
