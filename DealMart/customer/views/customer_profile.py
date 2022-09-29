"""PROFILE UPDATE PAGE"""
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import FormView,View
from django.shortcuts import render,redirect
from django.contrib import messages
from customer.mixins import CheckCustomerGroup
from django.core.exceptions import ValidationError
from user_module.forms import UserUpdate
from user_module.models import User
from customer.models import Cart


@method_decorator(login_required, name='dispatch')
class CustomerProfileUpdate(CheckCustomerGroup,FormView):
    """CUSTOMER PROFILE UPDATE PAGE"""
    title = ("Profile Update")
    template_name = "customer/customer_profile.html"
    form_class = UserUpdate



    def get(self,request):
        """GETTING DETAILS OF LOGGED USER"""
        form = UserUpdate(instance=request.user)
        cart = Cart.objects.filter(is_active=True,created_by = request.user).count()
        context = {
            'form':form,
            'cart':cart,
        }
        return render(request,self.template_name,context)

    def post (self,request):
        """OPERATION FOR UPDATING PROFILE OF USER"""
        user = request.user
        first_name =user.first_name = request.POST.get('first_name')
        last_name = user.last_name = request.POST.get('last_name')
        user.address = request.POST.get('address')
        phone = user.phone = request.POST.get('phone')

        if not first_name.isalpha():
            messages.error(request,"Invalid First name!")
            return redirect(request.path_info)
        
        if not last_name.isalpha():
            messages.error("Invalid Last name!")
            return redirect(request.path_info)

        if len(phone) < 10 :
            messages.error('Phone number must have atleast 10 digits')
            return redirect(request.path_info)

        if not first_name.isalpha():
            raise ValidationError("Invalid First name!")

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
