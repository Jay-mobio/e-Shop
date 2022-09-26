from django.shortcuts import render
from django.views.generic import ListView
from products.models import Inventory,Category
from customer.models import Cart
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class HomeView(ListView):
    template_name = 'authentication/home.html'
    model = Inventory
    paginate_by = 10


    def get(self,request):
        search = request.GET.get('search', "")
        ordering = request.GET.get('ordering',"")
        products = Inventory.objects.filter(is_active=True)
        cart = Cart.objects.filter(is_active=True,created_by = request.user)
        category = Category.objects.all()
        catid = request.GET.get('categories',"")

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

        context = {'products':products,'search':search,'page_number':page_number,'cart':cart,'category':category,'ordering':ordering}
        return render(request,self.template_name,context)