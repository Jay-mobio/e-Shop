"""UPDATE PRODUCT"""
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import HttpResponseRedirect,render,redirect
from django.contrib import messages
from django.views.generic import UpdateView,View
from product_admin.mixins import CheckProductOwnerGroup
from products.forms import AddProductForm
from products.models import Products
from customer.models import Cart

@method_decorator(login_required, name='dispatch')
class UpdateForm(CheckProductOwnerGroup,UpdateView):
    """UPDATE PRODUCT OPERATIONS"""
    template_name = "products/update_product.html"

    def get(self,request,pk):
        """GETTING DETAILS OF PRODUCT TO BE UPDATED"""
        product = Products.objects.get(id=pk)
        form = AddProductForm(instance=product)
        cart = Cart.objects.filter(created_by = request.user,is_active=True)
        context = {'form':form, 'product':product,'cart':cart}
        return render(request,self.template_name,context)

    def post(self,request,pk):
        """UPDATING PRODUCT DETAILS"""
        product = Products.objects.get(id=pk)
        product.name = request.POST.get('name')
        product.category_id = request.POST.get('category')
        sub_category = request.POST.get('sub_category')

        if sub_category == None:
            pass
        else:
            product.sub_category_id = sub_category

        product.brand = request.POST.get('brand')
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

class RemoveProductImage(View):
    """REMOVE PRODUCT IMAGE"""
    def post(self,request,pk):
        """REMOCING PRODUCT IMAGE"""
        product = Products.objects.get(id=pk)
        product.image = "static/images/default.jpg"
        product.save()

        messages.success(request,"Product has been updated succefully")

        return redirect("products:update_product_form",pk)
