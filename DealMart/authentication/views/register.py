from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.contrib import messages
from user_module.forms import UserRegister
from user_module.models import User
from authentication.views.otp import OTP
from django.contrib.auth.models import Group

class UserCreation(CreateView):
    title = ("Register Page")
    template_name: str = None
    form_class=None
    user_group: object = None
    redirect_url = None
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                messages.success(request,"User already exists") 
                return redirect(self.redirect_url)

            user = form.save()
            user.groups.add(self.user_group)
            user.is_active = False
            otp = OTP.generateotp(self,request,user)
            return render(request, 'authentication/otp.html', {'usr':user})
        context = {'form':form}
        return render(request, self.template_name, context)               


class ProductAdminRegisterView(UserCreation):
    title = ("Register Page")
    template_name = 'authentication/product_admin_register.html'
    form_class = UserRegister
    redirect_url = "authentication:product_admin_register"
    user_group = Group.objects.get(name='Product Owner')


class CustomerRegisterView(UserCreation):
    title = ("Register Page")
    template_name = 'authentication/register_page.html'
    form_class = UserRegister
    redirect_url = "authentication:otp"
    user_group = Group.objects.get(name='Customer')   
    