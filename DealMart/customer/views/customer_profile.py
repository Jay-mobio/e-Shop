"""PROFILE UPDATE PAGE"""
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import FormView,View
from django.shortcuts import render,redirect
from django.contrib import messages
from customer.mixins import CheckCustomerGroup
from user_module.forms import UserRegister
from user_module.models import User
from customer.models import Cart


@method_decorator(login_required, name='dispatch')
class CustomerProfileUpdate(CheckCustomerGroup,FormView):
    """CUSTOMER PROFILE UPDATE PAGE"""
    title = ("Profile Update")
    template_name = "customer/customer_profile.html"
    form_class = UserRegister



    def get(self,request):
        """GETTING DETAILS OF LOGGED USER"""
        form = UserRegister(instance=request.user)
        cart = Cart.objects.filter(is_active=True,created_by = request.user).only('id')
        context = {
            'form':form,
            'cart':cart,
        }
        return render(request,self.template_name,context)

    def post (self,request):
        """OPERATION FOR UPDATING PROFILE OF USER"""
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
        """GETTING SUCCESS URL"""
        return self.request.path

class CustomerRemoveProfileImage(View):
    """REMOVE PROFILE IMAGE"""
    def post(self,request,pk):
        """OPERATION FOR REMOVING PROFLE IMAGE"""
        user = User.objects.get(id=pk)
        user.profile_pic = "static/images/profile1.png"
        user.save()
        messages.success(request,"Product has been updated succefully")
        return redirect("customer:customer_profile")
