from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import Inventory



class Dashboard(TemplateView):
    template_name = "products/product_list.html"

    def get(self,request):
        products = Inventory.objects.filter(is_active=True)
        context = {'products':products}
        return render(request,self.template_name,context)