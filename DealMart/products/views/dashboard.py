"""DASHBOARD"""
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView
from products.models import Inventory,Category
from product_admin.mixins import CheckProductOwnerGroup
from customer.models import Cart

@method_decorator(login_required, name='dispatch')
class Dashboard(CheckProductOwnerGroup,ListView):
    """DASHBOARD OPERATIONS"""
    template_name = "products/product_list.html"
    model = Inventory
    paginate_by = 10

    def get(self,request):
        """GETTING LIST OF PRODUCTS"""
        products = Inventory.objects.filter(is_active=True)
        cart = Cart.objects.filter(is_active=True,created_by = request.user)
        search = request.GET.get('search', "")
        ordering = request.GET.get('ordering',"")
        catid = request.GET.get('categories',"")
        category = Category.objects.all().only('name')

        if ordering or catid or search is not None:
            products = self.get_queryset(ordering,catid,search,products)

        paginator  = Paginator(products,self.paginate_by)
        page_number = request.GET.get('page',1)
        products = paginator.get_page(page_number)

        context = {'products':products,'search':search,'page_number':page_number,'cart':cart,'category':category}
        return render(request,self.template_name,context)

    def get_queryset(self,ordering,catid,search,products):
        """GETTING QUERYSET FOR FILTER"""
        sort = {
            "low_to_high":'product__price',
            "high_to_low":'-product__price'
        }

        ordering =  sort[ordering] if ordering in sort else None

        if catid != "":
            products = products.filter(product__category = catid)
        else:
            pass

        if ordering is not None:
            products = products.order_by(ordering)
        else:
            pass

        if search != "":
            products = products.filter(product__name__icontains = search) | products.filter(product__brand__icontains=search)
        else:
            pass

        return products
