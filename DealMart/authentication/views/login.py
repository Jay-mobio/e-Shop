from django.views import View
from django.shortcuts import render
from django.contrib.auth import login 
from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import Group



class LoginView(View):
    template_name = "authentication/login_page.html"
    group = Group.objects.all()

    def get(self, request):
        return render(request,self.template_name)


    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email = email, password = password)
        if user:
            login(request, user)
            if user.groups.filter(name='Product Owner').exists():
                return redirect('authentication:home')
            return redirect('authentication:customer_page') 
        else:
            messages.error(request,'email or password not correct')
            return redirect('authentication:login')           







