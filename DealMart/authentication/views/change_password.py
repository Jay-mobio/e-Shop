from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.views.generic import FormView



class ChangePasswordView(FormView):

    template_name = "authentication/change_password.html"

    def get(self, request):
        return render(request,self.template_name)

    def post(self,request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password is successfully updated!')
            return redirect('authentication:logout')
        else:
            messages.error(request, 'Please correct the error below.')
            return redirect(request.path_info)
