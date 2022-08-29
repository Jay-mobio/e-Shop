from django.views.generic import DeleteView
from django.shortcuts import render,redirect
from products.models import Products
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

@method_decorator(login_required, name='dispatch')
class DeleteProduct(DeleteView):
    template_name = "products/product_list.html"

    def get(self,request,pk):
        product = Products.objects.get(id=pk)
        product.delete()        
        messages.success(request,"Product has been updated succefully")
        return redirect("products:dashboard")
