from products.forms import AddProductForm
from django.views.generic import FormView
from django.shortcuts import render,redirect
from products.models import Products
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class AddProduct(FormView):
    template_name = "products/add_product.html"
    form_class = AddProductForm
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

