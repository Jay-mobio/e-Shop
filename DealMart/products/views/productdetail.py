from products.forms import AddProductForm
from django.views.generic import DetailView
from django.shortcuts import render,redirect
from products.models import Products,Category,SubCategory
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class ProductDetail(DetailView):
    template_name = "products/update_product.html"

    def get(self,request,pk):
        product = Products.objects.get(id=pk)
        form = AddProductForm(instance=product)
        return render(request,self.template_name,{'form':form, 'product':product})

