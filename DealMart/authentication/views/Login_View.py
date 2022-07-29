from django.shortcuts import render
from django.contrib.auth import login
from django.views.generic.edit import FormView


class LoginView(FormView):
    def get(self,request):
        return render(request,"authentication/Login_page.html")
