from django.shortcuts import render
from django.views.generic import ListView
from products.models import Inventory
from django.core.paginator import Paginator
from products.models import Products
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from products.filters import ProductFilters




class Dashboard(ListView):
    template_name = "products/product_list.html"
    model = Products
    paginate_by = 2
    

    def get(self,request):
        search = request.GET.get('search', "")
        ordering = request.GET.get('ordering',"")
        products = Inventory.objects.filter(is_active=True)

        filtered_product = ProductFilters(
            request.GET,
            queryset= Inventory.objects.filter(is_active=True)
        )


        sort = {
            "low_to_high":'product__price',
            "high_to_low":'-product__price'
        }

        ordering =  sort[ordering] if ordering in sort else None
      
        if ordering != None and search != "":
            products = products.order_by(ordering)
            products = products.filter(product__name__icontains = search) | products.filter(product__brand__icontains=search)


        elif ordering == None and search != None:
            products = products.filter(product__name__icontains=search) | products.filter(product__brand__icontains=search)

        elif ordering != None:
            products = products.order_by(ordering)

            

        paginator  = Paginator(products,self.paginate_by)
        page_number = request.GET.get('page',1)
        finalproducts = paginator.get_page(page_number)

        context = {'products':products,'search':search,'finalproducts':finalproducts,'page_number':page_number,'filtered_product':filtered_product.qs}
        return render(request,self.template_name,context)
        

@csrf_exempt
def sort(request):
    ordering = request.GET.get('sortID')
    products = Dashboard.get(products)
    if ordering == 'low_to_high':
        products = products.order_by('price')
    elif ordering == 'high_to_low':
        products = products.order_by('-price')

    
    t = render_to_string('products/product_list.html', {'products': products})

    return JsonResponse({'data':t})

