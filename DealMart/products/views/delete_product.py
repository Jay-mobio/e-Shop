from django.views.generic import DeleteView
from django.shortcuts import redirect
from products.models import Products
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

@method_decorator(login_required, name='dispatch')
class DeleteProduct(DeleteView):

    def get(self,request,pk):
        product = Products.objects.get(id=pk)
        product.delete()        
        messages.success(request,"Product has been delete succefully")
        return redirect("products:dashboard")
