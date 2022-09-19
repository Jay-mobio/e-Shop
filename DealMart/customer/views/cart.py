from django.views.generic import ListView,DeleteView
from customer.models import Cart
from products.models import SubCategory
from django.shortcuts import render,redirect

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
            'total':total
        }
        return render(request,self.template_name,context)

class RemoveCartProduct(DeleteView):
    def get(self,request,pk):
        cart = Cart.objects.get(product=pk,is_active=True)
        cart.delete()
        return redirect('customer:cart')

