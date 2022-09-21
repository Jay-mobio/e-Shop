from re import sub
from django.shortcuts import redirect
from customer.models import Cart
from django.views.generic import UpdateView


class UpdateCart(UpdateView):
    
    def get(self,request,pk):
        sub_category = request.GET.get('sub_category')
        qty = request.GET.get('quantity')
        cart = Cart.objects.filter(id=pk,is_active=True)
        if qty == None:
            quantity = cart[0].quantity
        else:
            quantity = int(qty)
        if sub_category == None:
            sub_category = cart[0].size
        product_total = cart[0].product.price * quantity
        cart.update(size_id = sub_category,quantity = quantity,product_total=product_total)
      
        return redirect('customer:cart')
        
