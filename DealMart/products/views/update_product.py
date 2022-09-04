from products.forms import AddProductForm
from django.views.generic import UpdateView,View
from django.shortcuts import render,HttpResponseRedirect,redirect
from products.models import Products,Category,SubCategory
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError

@method_decorator(login_required, name='dispatch')
class UpdateForm(UpdateView):
    template_name = "products/update_product.html"

    def get(self,request,pk):
        product = Products.objects.get(id=pk)
        form = AddProductForm(instance=product)
        return render(request,self.template_name,{'form':form, 'product':product})

    def post(self,request,pk):
        product = Products.objects.get(id=pk)
        form = AddProductForm(instance=product)
        
        if form.is_valid():
            product.name = request.POST.get('name')
            category_id = request.POST.get('category')
            category = Category.objects.get(id=category_id)
            product.category = category
            sub_category_id = request.POST.get('sub_category')
            sub_category = SubCategory.objects.get(id=sub_category_id)
            brand = request.POST.get('brand')
            product.price = request.POST.get('price')
            try:
                product.image = request.FILES['image']
            except MultiValueDictKeyError:
                pass 
            product.discription  = request.POST.get('discription') 
            product.updated_by = request.user
            product.save()
            messages.success(request,"Product has been updated succefully")
            return HttpResponseRedirect(request.path_info)

        return render(request,self.template_name,{'form':form})

class RemoveProductImage(View):
    def post(self,request,pk):
        product = Products.objects.get(id=pk)
        product.image = "static/images/default.jpg"
        product.save()
        messages.success(request,"Product has been updated succefully")
        return redirect("products:update_product_form",pk)