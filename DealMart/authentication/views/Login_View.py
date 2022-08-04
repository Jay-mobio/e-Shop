from django.views import View
from django.shortcuts import render
from django.contrib.auth import login 
from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
from django.contrib import messages



class CustomLoginView(View):
    template_name = "authentication/login_page.html"

    def get(self, request):
        return render(request,self.template_name)


    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email = email, password = password)
        if user:
            login(request, user)
            return redirect('authentication:home')
        messages.error("email or password is wrong!", extra_tags="login_error")
        return render(request, self.template_name, context={'email': email})



