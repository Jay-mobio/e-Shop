"""
INVENTORY VIEW
"""
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView
from django.core.paginator import Paginator
from django.contrib import messages
from products.models import Inventory,Category
from product_admin.mixins import CheckProductOwnerGroup
from product_admin.forms import AddInventoryForm
from customer.models import Cart

@method_decorator(login_required, name='dispatch')
class InventoryList(CheckProductOwnerGroup,TemplateView):
    """ INVENTORY OPERATIONS """
    template_name = "product_admin/inventory_list.html"
    paginate_by = 10

    def get(self,request):
        """ GETTING INVENTORY LIST """
        products = Inventory.objects.filter(created_by=request.user).only
        ('product__name','product__price','product_quantity','product__brand','product__image')
        cart = Cart.objects.filter(created_by = request.user,is_active=True).count()
        search = request.GET.get('search', "")
        ordering = request.GET.get('ordering',"")
        catid = request.GET.get('categories',"")
        category = Category.objects.all().only('name')

        products = self.get_queryset(ordering,catid,search,products)

        paginator  = Paginator(products,self.paginate_by)
        page_number = request.GET.get('page',1)
        products = paginator.get_page(page_number)

        context = {'search':search,
                'page_number':page_number,
                'products':products,'cart':cart,
                'category':category}
        return render(request,self.template_name,context)

    def get_queryset(self,ordering,catid,search,products):
        """ GETTING QUERY """
        sort = {
            "low_to_high":'product__price',
            "high_to_low":'-product__price'
        }

        ordering =  sort[ordering] if ordering in sort else None

        if catid != "":
            products = products.filter(product__category = catid)

        if ordering is not None:
            products = products.order_by(ordering)

        if search != "":
            products = (products.filter(product__name__icontains = search) | products.filter(product__brand__icontains=search))

        return products


class UpdateInventory(CreateView):
    """ UPDATE INVENTORY OPERATIONS """
    template_name = "product_admin/inventory.html"

    def get(self,request,pk):
        """ GETTING DETAILS OF PRODUCT """
        inventory = Inventory.objects.get(product=pk)
        cart = Cart.objects.filter(created_by = request.user,is_active=True)
        form = AddInventoryForm(instance=inventory)
        context = {'form':form,'cart':cart,'inventory':inventory}
        return render(request,self.template_name,context)

    def post(self,request,pk):
        """ UPDATING INVENTORY OF PRODUCT """
        inventory = Inventory.objects.filter(product=pk,created_by=request.user)
        quantity = int(request.POST.get('product_quantity'))

        if quantity > 0 :
            is_active = True
        else :
            is_active = False

        inventory.update(product=pk,product_quantity=quantity,
                            is_active=is_active,updated_by=request.user)
        messages.success(request,"Product quantity Updated")
        return redirect(request.path_info)
