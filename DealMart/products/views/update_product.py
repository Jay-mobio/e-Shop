from products.forms import AddProductForm
from django.views.generic import UpdateView
from django.shortcuts import render,redirect
from products.models import Products
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class UpdateProduct(UpdateView):
    template_name = "products/update_product.html"

    def get(self,request,pk):
        product = Products.objects.get(id=pk)
        form = AddProductForm(instance=product)
        return render(request,self.template_name,{'form':form, 'product':product})

    
    def post(self,request,pk):
        product = Products.objects.get(id=pk)
        form = AddProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            product.name = form.cleaned_data.get('name')
            product.category = form.cleaned_data.get('category')
            product.price = form.cleaned_data.get('price')
            product.image = form.cleaned_data.get('image')
            product.discription  = form.cleaned_data.get('discription') 
            product.updated_by = request.user
            product.save()
            return redirect('authentication:home')
        return render(request,self.template_name,{'form':form})