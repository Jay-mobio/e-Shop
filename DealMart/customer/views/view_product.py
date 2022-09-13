from products.models import SubCategory
from products.models import Products
from customer.models import Cart
from products.forms import AddProductForm
from django.views.generic import DetailView
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class ProductView(DetailView):
    template_name = "customer/product_view.html"

    def get(self,request,pk):
        product = Products.objects.get(pk=pk)
        sub_categorys = SubCategory.objects.filter(category = product.category)
        form = AddProductForm(initial={'name':product.name, 'category':product.category, 'discription':product.discription})
        return render(request,self.template_name,{'form':form, 'product':product, 'sub_categorys':sub_categorys})

    def post(self,request,pk):
        product = Products.objects.get(pk=pk)
        form = AddProductForm(instance=product)
        if form.is_valid():
            quantity = request.POST.get('quantity')
            sub_category = request.POST.get('sub_category')

            print(sub_category)
            sub_category = request.POST.get('sub_category')
            product_total = int(quantity)*product.price
            Cart.objects.create(product=product,created_by=request.user,quantity=quantity,product_total=product_total)
            messages.success(request,"Product Has Been Added To Cart")
            return redirect(request.path_info)
