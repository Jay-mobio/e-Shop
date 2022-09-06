import json
from django.shortcuts import render
from django.views.generic import ListView
from products.models import Inventory
from django.http import JsonResponse
from customer.models import Cart

class Cart(ListView):
    template_name = "customer/cart.html"



    def get(self,request,pk):
        product = Cart.objects.get(id=pk)
        
        return render(request,self.template_name,{'product':product})

    def post(self,request,pk):
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']
        print('Action:', action)
        print('Product:', productId)

        product = Inventory.objects.get(id=pk)

        if action == 'add':
            product = (product.quantity + 1)
        elif action == 'remove':
            product = (product.quantity - 1)

        product.save()

        if product.quantity <= 0:
            product.delete()

        return JsonResponse('Item was added', safe=False)