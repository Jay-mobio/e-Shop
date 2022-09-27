from products.forms import AddProductForm
from django.views.generic import DetailView
from django.shortcuts import render
from products.models import Inventory
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from customer.models import Cart

@method_decorator(login_required, name='dispatch')
class ProductOrder(DetailView):
    template_name = "products/product_detail.html"

    def get(self,request,pk):
        product = Inventory.objects.get(pk=pk)
        cart = Cart.objects.filter(created_by = request.user,is_active=True).only('id')
        form = AddProductForm(instance=product)
        context = {'form':form, 'product':product,'cart':cart}
        
        return render(request,self.template_name,context)

