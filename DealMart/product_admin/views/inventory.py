from operator import truediv
from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView
from products.models import Products,Inventory,Category
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
        products = Inventory.objects.filter(created_by=request.user)
        search = request.GET.get('search', "")
        ordering = request.GET.get('ordering',"")
        cart = Cart.objects.filter(created_by = request.user,is_active=True)
        
        category = Category.objects.all()
        search = request.GET.get('search', "")
        ordering = request.GET.get('ordering',"")
        catid = request.GET.get('categories',"")

        sort = {
            "low_to_high":'product__price',
            "high_to_low":'-product__price'
        }
        if ordering == 'is_active':
            products = products.filter(is_active = True)
        
        if ordering == 'is_not_active':  
            products = products.filter(is_active = False)

        ordering =  sort[ordering] if ordering in sort else None

        if catid != "":
            products = products.filter(product__category = catid)
        else:
            pass

        if ordering != None:
            products = products.order_by(ordering)
        else:
            pass

        if search != "":
            products = products.filter(product__name__icontains = search) | products.filter(product__brand__icontains=search)
        else:
            pass

            

        paginator  = Paginator(products,self.paginate_by)   
        page_number = request.GET.get('page',1)
        products = paginator.get_page(page_number)

        context = {'products':products,'search':search,'page_number':page_number,'products':products,'cart':cart,'category':category}
        return render(request,self.template_name,context)

class UpdateInventory(CreateView):
    template_name = "product_admin/inventory.html"

    def get(self,request,pk):
        product = Products.objects.get(id=pk)
        inventory = Inventory.objects.get(product=product)
        cart = Cart.objects.filter(created_by = request.user,is_active=True)
        form = AddInventoryForm(instance=product)
        context = {'form':form,'product':product,'cart':cart,'inventory':inventory}
        return render(request,self.template_name,context)

    def post(self,request,pk):
        product = Products.objects.get(id=pk)
        form = AddInventoryForm(instance=product)
        inventory = Inventory.objects.filter(product=product,created_by=request.user)
        product_quantity = request.POST.get('product_quantity')
        quantity = int(product_quantity)
        
        if quantity > 0 :
            is_active = True
        else :
            is_active = False
        
        inventory.update(product=product,product_quantity=quantity,is_active=is_active,updated_by=request.user)
        messages.success(request,"Product quantity Updated")
        return redirect(request.path_info)