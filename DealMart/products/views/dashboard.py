from django.shortcuts import render
from django.views.generic import ListView
from products.models import Inventory
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from products.models import Products
from django.db.models import Q



class Dashboard(ListView):
    template_name = "products/product_list.html"
    model = Products
    paginate_by = 3
    ordering = ['ordering']

    def get(self,request):
        products = Inventory.objects.filter(is_active=True) 
        search = request.GET.get('search', "")
        products = Inventory.objects.filter(product__name__icontains=search)
        multiple_q = Q(Q(product__name__icontains=search) | Q(product__brand__icontains=search))
        products = Inventory.objects.filter(multiple_q)
        paginator  = Paginator(products,self.paginate_by)
        page_number = request.GET.get('page',1)
        finalproducts = paginator.get_page(page_number)
        context = {'products':products,'search':search,'finalproducts':finalproducts,'page_number':page_number}
        return render(request,self.template_name,context)