from django.views.generic import DeleteView
from django.shortcuts import render,redirect
from products.models import Products
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class DeleteProduct(DeleteView):
    template_name = "products/delete_product.html"
    def get(self,request,pk):
        product = Products.objects.get(id=pk)
        return render(request,self.template_name,{'product':product})

    def post(self,request,pk):
        product = Products.objects.get(id=pk)
        product.delete()        
        return redirect('products:dashboard')