from re import sub
from django.shortcuts import redirect
from customer.models import Cart
from django.views.generic import UpdateView


class UpdateCart(UpdateView):
    
    def get(self,request,pk):
        sub_category = request.GET.get('sub_category')
        quantity = request.GET.get('quantity')
        cart = Cart.objects.filter(id=pk,is_active=True)

        if quantity == None:
            quantity = cart[0].quantity
        if sub_category == None:
            sub_category = cart[0].size
        cart.update(size_id = sub_category,quantity = quantity)
      
        return redirect('customer:cart')
        
