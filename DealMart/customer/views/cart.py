from django.views.generic import ListView,DeleteView
from customer.models import Cart
from products.models import SubCategory
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect

class ListCart(ListView):
    template_name = "customer/cart.html"

    def get(self,request):
        cart = Cart.objects.filter(is_active=True)
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

# @csrf_exempt
# def addtocart(request, id):
#     # if request.method=='POST':
#     # product_id = id)
#     # if (Cart.objects.filter(user=request.user.id,product_id=id)):
#     #     return JsonResponse({'status':"Product Already in Cart"})
#     # else:
#     #     quantity = product.quantity + 1
#     #     Cart.objects.create(user=request.user,product_id=id,quantity=quantity)
#     #     # return JsonResponse({'status':"Product has been added in Cart"})
    
#     product = Products.objects.get(id=id)
#     Cart.objects.create(product=product,created_by=request.user)
#     return JsonResponse({'status':200})









    # template_name = "customer/cart.html"



    # def get(self,request,pk):
    #     product = Cart.objects.get(id=pk)
        
    #     return render(request,self.template_name,{'product':product})

    # def post(self,request,pk):
    #     data = json.loads(request.body)
    #     productId = data['productId']
    #     action = data['action']
    #     print('Action:', action)
    #     print('Product:', productId)

    #     product = Inventory.objects.get(id=pk)

    #     if action == 'add':
    #         product = (product.quantity + 1)
    #     elif action == 'remove':
    #         product = (product.quantity - 1)

    #     product.save()

    #     if product.quantity <= 0:
    #         product.delete()

    #     return JsonResponse('Item was added', safe=False)
