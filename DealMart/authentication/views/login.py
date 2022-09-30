"""LOGIN PAGE"""
from django.views import View
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
from django.contrib import messages
from user_module.models import User
from authentication.views.otp import OTP



class LoginView(View):
    """LOGIN PAGE"""
    template_name = "authentication/login_page.html"

    def get(self,request):
        """RENDERING LOGIN PAGE"""
        return render(request,self.template_name)

    def post(self, request):
        """GETTING LOGIN CREDENTIALS"""
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.get(email=email)
        if user:
            if not user.is_active:
                OTP.generateotp(self,user)
                return render(request,"authentication/otp.html",{'usr':user})

            authenticated_user = authenticate(email = email, password = password)
            if authenticated_user:
                login(request, authenticated_user)
                if user.groups.filter(name='Product Owner').exists():
                    return redirect('products:dashboard')
                return redirect('authentication:home')
            else:
                messages.error(request,'Email or password is incorrect')
                return redirect('authentication:login')
        messages.error(request,"User dose not exist")
        return redirect('authentication:login')
