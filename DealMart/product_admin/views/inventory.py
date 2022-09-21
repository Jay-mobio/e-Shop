from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView
from products.models import Products,Inventory
from product_admin.forms import AddInventoryForm
from django.core.paginator import Paginator
from product_admin.mixins import CheckProductOwnerGroup
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from customer.models import Cart

@method_decorator(login_required, name='dispatch')
class InventoryList(CheckProductOwnerGroup,TemplateView):
    template_name = "product_admin/inventory_list.html"
    paginate_by = 10
    

    def get(self,request):
        products = Products.objects.filter(created_by=request.user)
        search = request.GET.get('search', "")
        ordering = request.GET.get('ordering',"")
        cart = Cart.objects.filter(created_by = request.user,is_active=True)

        sort = {
            "low_to_high":'price',
            "high_to_low":'-price'
        }

        ordering =  sort[ordering] if ordering in sort else None
      
        if ordering != None and search != "":
            products = products.order_by(ordering)
            products = products.filter(name__icontains = search) | products.filter(brand__icontains=search)


        elif ordering == None and search != None:
            products = products.filter(name__icontains=search) | products.filter(brand__icontains=search)

        elif ordering != None:
            products = products.order_by(ordering)

            

        paginator  = Paginator(products,self.paginate_by)   
        page_number = request.GET.get('page',1)
        products = paginator.get_page(page_number)

        context = {'products':products,'search':search,'page_number':page_number,'products':products,'cart':cart}
        return render(request,self.template_name,context)

class AddInventory(CreateView):
    template_name = "product_admin/inventory.html"
    form_class = AddInventoryForm

    def get(self,request,pk):
        product = Products.objects.get(id=pk)
        cart = Cart.objects.filter(created_by = request.user,is_active=True)
        form = self.form_class
        context = {'form':form,'product':product,'cart':cart}
        return render(request,self.template_name,context)

    def post(self,request,pk):
        form_class = AddInventoryForm
        product = Products.objects.get(product=pk)
        product_quantity = request.POST.get('product_quantity')
        is_active = False
        if product_quantity != 0 :
            is_active = True
        
        Inventory.objects.create(product=product,is_active=is_active,created_by=request.user)