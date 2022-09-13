from django.shortcuts import redirect
from customer.models import Cart
from django.views.generic import UpdateView


class UpdateCart(UpdateView):
    
    def get(self,request,pk):
        cart = Cart.objects.filter(product=pk,is_active=True)
        cart[0].product.sub_category = request.GET.get('sub_category')
        cart[0].quantity = request.GET.get('quantity')
        cart[0].save()

        
        return redirect('customer:cart')
        
