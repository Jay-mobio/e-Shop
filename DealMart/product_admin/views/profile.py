from user_module.models import User
from django.views.generic import FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from user_module.forms import UserRegister
from django.shortcuts import render,redirect


# @method_decorator(login_required, name='dispatch')
class ProfileUpdate(FormView):
    title = ("Profile Update")
    template_name = "profile_update.html"
    form_class = UserRegister

    def get(self,request,pk):
        product = User.objects.get(id=pk)
        form = UserRegister(instance=product)
        return render(request,self.template_name,{'form':form})

