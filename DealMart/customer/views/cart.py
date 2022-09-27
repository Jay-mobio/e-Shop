from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView,DeleteView
from django.shortcuts import render,redirect
from products.models import SubCategory
from customer.models import Cart


@method_decorator(login_required, name='dispatch')
class ListCart(ListView):
    template_name = "customer/cart.html"
    

    def get(self,request):
        cart = Cart.objects.filter(is_active=True,created_by = request.user).only('id','product_id','product__image','product__name','product__price','quantity','product_total','size')
        total = 0
        sub_categories = []
        if len(cart) > 0:
            total = self.get_total(cart)
            sub_categories = self.get_sub_categories(cart)

        context = {
            'mylist': zip(cart, sub_categories),
            'total':total,
            'cart':cart
        }
        return render(request,self.template_name,context)
    
    def get_total(self,cart):
        total = 0
        for i in cart:
            total = i.product.price * i.quantity + total
        return total
    
    def get_sub_categories(self,cart):
        sub_categories = []
        for i in cart:
            sub_category = SubCategory.objects.filter(category = i.product.category).only('id','name')
            sub_categories.append(sub_category)
        return sub_categories


class RemoveCartProduct(DeleteView):
    def get(self,request,pk):
        cart = Cart.objects.get(id=pk,is_active=True)
        cart.delete()
        return redirect('customer:cart')

