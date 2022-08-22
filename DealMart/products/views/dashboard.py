from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import Products



class Dashboard(TemplateView):
    template_name = "products/product_list.html"

    def get(self,request):
        products = Products.objects.all()   
        context = {'products':products}
        return render(request,self.template_name,context)