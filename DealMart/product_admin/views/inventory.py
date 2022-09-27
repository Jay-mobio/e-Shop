from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,TemplateView
from products.models import Products,Inventory,Category
from product_admin.mixins import CheckProductOwnerGroup
from django.utils.decorators import method_decorator
from product_admin.forms import AddInventoryForm
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.contrib import messages
from customer.models import Cart

@method_decorator(login_required, name='dispatch')
class InventoryList(CheckProductOwnerGroup,TemplateView):
    template_name = "product_admin/inventory_list.html"
    paginate_by = 10
    
    def get(self,request):
        products = Inventory.objects.filter(created_by=request.user).only('product__name','product__price','product_quantity','product__brand','product__image')
        cart = Cart.objects.filter(created_by = request.user,is_active=True).only('id')
        search = request.GET.get('search', "")
        ordering = request.GET.get('ordering',"")
        catid = request.GET.get('categories',"")
        category = Category.objects.all().only('name')

        sort = {
            "low_to_high":'product__price',
            "high_to_low":'-product__price'
        }

        if ordering == 'is_active':
            products = products.filter(is_active = True)
        
        if ordering == 'is_false':  
            products = products.filter(is_active = False)
            

        ordering =  sort[ordering] if ordering in sort else None

        if catid != "":
            products = products.filter(product__category = catid)
        else:
            pass

        if ordering:
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
        inventory = Inventory.objects.get(product=pk)
        cart = Cart.objects.filter(created_by = request.user,is_active=True)
        form = AddInventoryForm(instance=inventory)
        context = {'form':form,'cart':cart,'inventory':inventory}
        return render(request,self.template_name,context)

    def post(self,request,pk):
        inventory = Inventory.objects.filter(product=pk,created_by=request.user)
        quantity = int(request.POST.get('product_quantity'))
        
        if quantity > 0 :
            is_active = True
        else :
            is_active = False
        
        inventory.update(product=pk,product_quantity=quantity,is_active=is_active,updated_by=request.user)
        messages.success(request,"Product quantity Updated")
        return redirect(request.path_info)