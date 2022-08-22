from unicodedata import category, name
from products.forms import AddProductForm
from django.views.generic import FormView,UpdateView,DeleteView,View
from django.shortcuts import render,redirect
from products.models import Products
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse


class AddProduct(FormView):
    template_name = "products/add_product.html"
    form_class = AddProductForm
    @method_decorator(login_required)
    def get(self,request):
        form = self.form_class
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form  = AddProductForm(request.POST,request.FILES)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            category = form.cleaned_data.get('category')
            price = form.cleaned_data.get('price')
            image = form.cleaned_data.get('image')
            discription  = form.cleaned_data.get('discription')
            created_by = request.user
            Products.objects.create(name=name,category=category,price=price,image=image,discription=discription,created_by=created_by)
            return redirect('authentication:home')
        return render(request,self.template_name,{'form':form})

class UpdateProduct(UpdateView):
    template_name = "products/update_product.html"
    model = Products
    fields = ['name','category','price','image','discription']


    def get(self,request,pk):
        product = Products.objects.get(id=pk)
        form = AddProductForm(instance=product)
        return render(request,self.template_name,{'form':form})

    
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

class DeleteProduct(DeleteView):
    template_name = "products/delete_product.html"

    def get(self,request,pk):
        product = Products.objects.get(id=pk)
        return render(request,self.template_name,{'product':product})

    def post(self,request,pk):
        product = Products.objects.get(id=pk)
        product.delete()        
        return redirect('products:dashboard')
