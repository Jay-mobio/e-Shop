from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from customer.mixins import CheckCustomerGroup
from django.views.generic import FormView,View
from django.shortcuts import render,redirect
from user_module.forms import UserRegister
from user_module.models import User
from django.contrib import messages
from customer.models import Cart


@method_decorator(login_required, name='dispatch')
class CustomerProfileUpdate(CheckCustomerGroup,FormView):
    title = ("Profile Update")
    template_name = "customer/customer_profile.html"
    form_class = UserRegister



    def get(self,request):
        form = UserRegister(instance=request.user)
        cart = Cart.objects.filter(is_active=True,created_by = request.user).only('id')
        context = {
            'form':form,
            'cart':cart,
        }
        return render(request,self.template_name,context)

    def post (self,request):
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.address = request.POST.get('address')
        user.phone = request.POST.get('phone')

        try:
            user.profile_pic = request.FILES['profile_pic']
        except MultiValueDictKeyError:
            pass 
        user.updated_by = request.user
        user.save()

        messages.success(request,"Your Profile has been updated succefully")
        return redirect(request.path_info)
        

    def get_success_url(self):
        return self.request.path

        
class CustomerRemoveProfileImage(View):
    def post(self,request,pk):
        user = User.objects.get(id=pk)
        user.profile_pic = "static/images/profile1.png"
        user.save()
        messages.success(request,"Product has been updated succefully")
        return redirect("customer:customer_profile")