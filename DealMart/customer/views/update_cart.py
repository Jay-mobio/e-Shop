"""UPDATE CART"""
from django.views.generic import UpdateView
from django.shortcuts import redirect
from django.contrib import messages
from customer.models import Cart


class UpdateCart(UpdateView):
    """UPDATE CART OPERATIONS"""
    def get(self,request,pk):
        """GETTING DETAILS OF PRODUCT TO BE UPDATED IN CART"""
        sub_category = request.GET.get('sub_category')
        quantity = int(request.GET.get('quantity'))
        cart = Cart.objects.filter(id=pk,is_active=True).only('id','product_id','product__name','size','quantity')

        if quantity is None :
            quantity = cart[0].quantity

        if sub_category is None:
            sub_category = cart[0].size

        if quantity is None and sub_category is None:
            return redirect(request.path_info)

        product_total = self.get_product_total(cart,quantity)
        cart.update(size_id = sub_category,quantity = quantity,product_total=product_total)

        messages.success(request,"Cart updated")
        return redirect('customer:cart')

    def get_product_total(self,cart,quantity):
        """GETTING TOTAL OF CART"""
        product_total = 0
        product_total = cart[0].product.price * quantity
        return product_total
