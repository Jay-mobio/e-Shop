from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Group

class CustomerView(TemplateView):
    template_name = "authentication/customer_page.html"
    
    @method_decorator(login_required)
    def get(self,request):
        group = Group.objects.get(name="Customer")
        usr = request.user
        if usr.groups is not None:
            usr.groups.add(group)
            usr.save()
        return render(request,self.template_name)
