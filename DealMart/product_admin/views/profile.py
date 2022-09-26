from user_module.models import User
from django.views.generic import FormView,View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from user_module.forms import UserRegister
from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from product_admin.mixins import CheckProductOwnerGroup
from customer.models import Cart




@method_decorator(login_required, name='dispatch')
class ProfileUpdate(CheckProductOwnerGroup,FormView):
    title = ("Profile Update")
    template_name = "product_admin/profile.html"
    form_class = UserRegister

    def get(self,request):
        form = UserRegister(instance=request.user)
        cart = Cart.objects.filter(created_by = request.user,is_active=True)
        context = {'form':form,'cart':cart}
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

        messages.success(request,"Profile has been updated succefully")
        return redirect(request.path_info)
    

    def get_success_url(self):
        return self.request.path


        
class RemoveProfileImage(View):
    def post(self,request,pk):
        user = User.objects.get(id=pk)
        user.profile_pic = "static/images/profile1.png"
        user.save()
        messages.success(request,"Product has been updated succefully")
        return redirect("product_admin:profile")