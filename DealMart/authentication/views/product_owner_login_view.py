from django.views import View
from django.shortcuts import render
from django.contrib.auth import login 
from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import Group



class ProductOwnerLoginView(View):
    template_name = "authentication/product_owner_login_page.html"
    group = Group.objects.all()

    def get(self, request):
        return render(request,self.template_name)


    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email = email, password = password)
        if user is not None:
            if user.groups.filter(name='Product Owner').exists():
                if user:
                    login(request, user)
                    return redirect('authentication:home')
            else:
                messages.error(request,'seems like you are in wrong login page')
                return redirect('authentication:product_owner_login')
        else:
            messages.error(request,'username or password not correct')
            return redirect('authentication:product_owner_login')
        return render(request, self.template_name, context={'email': email})



