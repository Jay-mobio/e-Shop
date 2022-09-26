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
        cart = Cart.objects.filter(is_active=True,created_by = request.user)
        total = 0
        sub_categorys = []
        for i in cart:
            total = i.product.price * i.quantity + total
            sub_category = SubCategory.objects.filter(category = i.product.category)
            sub_categorys.append(sub_category)
            
        context = {
            'mylist': zip(cart, sub_categorys),
            'total':total,
            'cart':cart
        }
        return render(request,self.template_name,context)

class RemoveCartProduct(DeleteView):
    def get(self,request,pk):
        cart = Cart.objects.get(id=pk,is_active=True)
        cart.delete()
        return redirect('customer:cart')

