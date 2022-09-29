"""HOME PAGE"""
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator
from products.models import Inventory,Category
from customer.models import Cart


@method_decorator(login_required, name='dispatch')
class HomeView(ListView):
    """HOME PAGE"""
    template_name = 'authentication/home.html'
    model = Inventory
    paginate_by = 10


    def get(self,request):
        """GETTING LIST OF PRODUCTS TO DISPLAY IN HOME PAGE"""
        catid = request.GET.get('categories',"")
        search = request.GET.get('search', "")
        ordering = request.GET.get('ordering',"")
        products = Inventory.objects.filter(is_active=True).only('product_id','product__image',
        'product__name','product__price','product__brand')
        cart = Cart.objects.filter(is_active=True,created_by = request.user).count()
        category = Category.objects.all().only('id','name')

        products = self.get_queryset(ordering,catid,search,products)

        paginator  = Paginator(products,self.paginate_by)
        page_number = request.GET.get('page',1)
        products = paginator.get_page(page_number)

        context = {'products':products,'search':search,'page_number':page_number,
                    'cart':cart,'category':category,'ordering':ordering}
        return render(request,self.template_name,context)

    def get_queryset(self,ordering,catid,search,products):
        """GETTING QUERYSET FOR FILTERING PRODUCTS"""
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
            products = products.filter(product__name__icontains = search) | products.filter(product__brand__icontains=search)

        return products
