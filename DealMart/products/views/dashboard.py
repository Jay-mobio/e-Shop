from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import Inventory
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from products.models import Products
from products.filters import ProductFilter
from django.db.models import Q



class Dashboard(TemplateView):
    template_name = "products/product_list.html"
    paginate_by = 20
    model = Products

    def get(self,request):
        products = Inventory.objects.filter(is_active=True)
        search = request.GET.get('q', "")
        products = Inventory.objects.filter(product__name__icontains=search)
        multiple_q = Q(Q(product__name__icontains=search) | Q(product__brand__icontains=search))
        products = Inventory.objects.filter(multiple_q)
        paginator  = Paginator(products,3)
        page_number = request.GET.get('page')
        finalproducts = paginator.get_page(page_number)
        context = {'products':products,'search':search,'finalproducts':finalproducts,'page_number':page_number}
        return render(request,self.template_name,context)