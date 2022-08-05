from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class CustomerView(TemplateView):
    template_name = "authentication/customer_page.html"

    @method_decorator(login_required)
    def get(self, request):
        return render(request,self.template_name)