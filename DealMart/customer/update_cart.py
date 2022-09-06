from math import fabs
from products.models import Inventory
from django.core.exceptions import ObjectDoesNotExist
from customer.models import Cart
from django.shortcuts import redirect
from django.views.generic import CreateView,DeleteView
from django.http import JsonResponse

class AddToCart(CreateView):
    def post(self,request,pk):
        try:
            cart = Inventory.objects.get(id=pk)
        except ObjectDoesNotExist:
            pass
        else :
            try:
                cart = Cart.objects.get(user = request.user, active = True)
            except ObjectDoesNotExist:
                cart = Cart.objects.create(user = request.user)
                cart.save()
                cart.add_to_cart(pk)
                return redirect('customer:cart')
            else:
                return redirect('authentication:home')

class DeleteFromCart(DeleteView):
    def post(request, book_id):
        if request.user.is_authenticated():
            try:
                book = Inventory.objects.get(pk = book_id)
            except ObjectDoesNotExist:
                pass 
            else:
                cart = Cart.objects.get(user = request.user, active = True)
                cart.remove_from_cart(book_id)
            return redirect('customer:cart')
        else:
            pass


def updateitem(request):
    return JsonResponse('Item added to cart', safe=False)