from django.views.generic import TemplateView
from django.shortcuts import render

class nav(TemplateView):
    template_name = "products/navbar.html"
    def get(self,request):
        return render(request,self.template_name)