from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




class HomeView(TemplateView):
    @method_decorator(login_required)
    def get(self, request):
        return render(request,'product_admin/home.html')   