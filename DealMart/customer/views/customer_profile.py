from user_module.models import User
from django.views.generic import FormView,View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from user_module.forms import UserRegister
from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from customer.mixins import CheckCustomerGroup
from django.core.exceptions import ValidationError





@method_decorator(login_required, name='dispatch')
class CustomerProfileUpdate(CheckCustomerGroup,FormView):
    title = ("Profile Update")
    template_name = "customer/customer_profile.html"
    form_class = UserRegister



    def get(self,request):
        form = UserRegister(instance=request.user)
        return render(request,self.template_name,{'form':form})

    def post (self,request):
        user = request.user
        form = UserRegister(instance=user)


        if form.is_valid():
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.address = request.POST.get('address')
            phone = user.phone = request.POST.get('phone')

            if not user.first_name.isalpha():
                messages.error(request,"Inavlid First Name")
                return redirect(request.path_info)

            if not user.last_name.isalpha():
                messages.error(request,"Invalid Last name!")
                return redirect(request.path_info)
            if not user.phone.isdigit():
                messages.error(request,"Please Enter Valid Mobile Number")
                return redirect(request.path_info)
            if len(phone) < 10 :
                messages.error(request,"Phone not valid")
                return redirect(request.path_info)

            try:
                user.profile_pic = request.FILES['profile_pic']
            except MultiValueDictKeyError:
                pass 
            user.updated_by = request.user
            user.save()

            messages.success(request,"Profile has been updated succefully")
            return redirect(request.path_info)
        

        return render(request,self.template_name,{'form':form})

    def get_success_url(self):
        return self.request.path


@method_decorator(login_required, name='dispatch')
class SocialCustomerProfileUpdate(CheckCustomerGroup,FormView):
    title = ("Profile Update")
    template_name = "customer/social_profile.html"
    form_class = UserRegister



    def get(self,request):
        form = UserRegister(instance=request.user)
        return render(request,self.template_name,{'form':form})

    def post (self,request):
        print("post")
        user = request.user
        form = UserRegister(instance=user)


        if form.is_valid():
            print("form")

            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.email = request.POST.get('email')
            user.address = request.POST.get('address')
            user.phone = request.POST.get('phone')

            try:
                user.profile_pic = request.FILES['profile_pic']
            except MultiValueDictKeyError:
                pass 
            user.updated_by = request.user
            user.save()

            messages.success(request,"Profile has been updated succefully")
            return redirect(request.path_info)
        

        return render(request,self.template_name,{'form':form})

    def get_success_url(self):
        return self.request.path

        
class CustomerRemoveProfileImage(View):
    def post(self,request,pk):
        user = User.objects.get(id=pk)
        user.profile_pic = "static/images/profile1.png"
        user.save()
        messages.success(request,"Product has been updated succefully")
        return redirect("customer:customer_profile")