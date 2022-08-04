import django
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.views import View
from user_module.models import User
from authentication.forms import CustomPwdChgForm
from django.contrib.auth import login


class ChangePasswordView(View):

    template_name = "authentication/change_password.html"

    def get(self, request):
        return render(request,self.template_name)


    def post(self,request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('authentication:home')
        else:
                messages.error(request, 'Please correct the error below.')
        form = CustomPwdChgForm(request.user)
        return render(request, 'authentication/change_password.html', {
            'form': form
                })
