"""CART LIST"""
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView,DeleteView
from django.shortcuts import render,redirect
from products.models import SubCategory
from customer.models import Cart


@method_decorator(login_required, name='dispatch')
class ListCart(ListView):
    """CART OPEATIONS"""
    template_name = "customer/cart.html"

    def get(self,request):
        """GETTING CART PRODUCT LIST"""
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
        """GETTING TOTAL OF CART"""
        total = 0
        for i in cart:
            total = i.product.price * i.quantity + total
        return total

    def get_sub_categories(self,cart):
        """GETTING QUERYSET FOR CART"""
        sub_categories = [SubCategory.objects.filter(category = i.product.category).only('id','name') for i in cart]
        return sub_categories


class RemoveCartProduct(DeleteView):
    """REMOVE CART PRODUCT"""
    def get(self,pk):
        """GETTING DETAILS OF PRODUCT TO BE REMOVED"""
        cart = Cart.objects.get(id=pk,is_active=True)
        cart.delete()
        return redirect('customer:cart')
