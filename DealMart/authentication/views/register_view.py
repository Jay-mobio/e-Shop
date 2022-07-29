from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.contrib import messages
from authentication.forms import UserRegister
from django.contrib.auth.models import User


class RegisterView(CreateView):
    title = ("Register Page")
    template_name = "/authentication/register_page.html"
    form_class = UserRegister

    def get (self,request):
        form = UserRegister
        if request.method == 'POST':
            form = UserRegister(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                return redirect('authentication:login')
        context = {'form':form}
        return render(request,'authentication/register_page.html')
