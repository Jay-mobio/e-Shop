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
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            if not user.is_active:
                OTP.generateotp(self,request,user)
                return render(request,"authentication/otp.html",{'usr':user})

            user = authenticate(email = email, password = password)
            if user:
                login(request, user)
                if user.groups.filter(name='Product Owner').exists():
                    return redirect('products:dashboard')
                return redirect('authentication:home')
            else:
                messages.error(request,'Email or password is incorrect')
                return redirect('authentication:login')
        messages.error(request,"User dose not exist")
        return redirect('authentication:login')
