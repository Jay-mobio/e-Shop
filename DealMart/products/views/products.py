from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
from product_admin.mixins import CheckProductOwnerGroup
from django.utils.decorators import method_decorator
from products.models import Inventory,Products
from django.shortcuts import render,redirect
from products.forms import AddProductForm
from django.views.generic import FormView
from django.contrib import messages
from customer.models import Cart



@method_decorator(login_required, name='dispatch')
class AddProduct(CheckProductOwnerGroup,FormView):

    template_name = "products/add_product.html" 
    form_class = AddProductForm

    def get(self,request):
        form = self.form_class
        cart = Cart.objects.filter(created_by = request.user,is_active=True)
        context = {'form':form,'cart':cart}
        return render(request,self.template_name,context)



    def post(self,request):

        form  = AddProductForm(request.POST,request.FILES)

        if form.is_valid(): 
            try:
                images = request.FILES['image']
            except MultiValueDictKeyError:
                images = "static/images/default.jpg"                
        
            name = request.POST.get('name')
            category = request.POST.get('category')  
            sub_category = request.POST.get('sub_category')
            brand = request.POST.get('brand')
            price = request.POST.get('price')
            discription  = request.POST.get('discription')
            created_by = request.user
            inventory = Products.objects.create(name=name,category_id=category,price=price,discription=discription,created_by=created_by,sub_category_id=sub_category,brand=brand,image=images)
            Inventory.objects.create(product=inventory,created_by=request.user)
            messages.success(request,"Product has been successfully added")
            return redirect('products:dashboard')
        context = {'form':form}
        return render(request,self.template_name,context)