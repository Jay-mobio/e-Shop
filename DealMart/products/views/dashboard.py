from django.contrib.auth.decorators import login_required
from product_admin.mixins import CheckProductOwnerGroup
from django.utils.decorators import method_decorator
from products.models import Inventory,Category
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.shortcuts import render
from customer.models import Cart    

@method_decorator(login_required, name='dispatch')
class Dashboard(CheckProductOwnerGroup,ListView):
    template_name = "products/product_list.html"
    model = Inventory
    paginate_by = 10
    

    def get(self,request):
        products = Inventory.objects.filter(is_active=True)
        cart = Cart.objects.filter(is_active=True,created_by = request.user)
        search = request.GET.get('search', "")
        ordering = request.GET.get('ordering',"")
        catid = request.GET.get('categories',"")
        category = Category.objects.all()

        sort = {
            "low_to_high":'product__price',
            "high_to_low":'-product__price'
        }

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

        context = {'products':products,'search':search,'page_number':page_number,'cart':cart,'category':category}
        return render(request,self.template_name,context)
        

