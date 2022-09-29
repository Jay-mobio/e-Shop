"""CHANGE PASSWORD"""
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.views.generic import FormView



class ChangePasswordView(FormView):
    """CHANGE PASSWORD OPERATIONS"""

    template_name = "authentication/change_password.html"

    def get(self, request):
        """RENDERING TEMPLATE FOR CHANGING PASSWORD"""
        return render(request,self.template_name)

    def post(self,request):
        """FORM VALIDATION FOR CHANGING PASSWORD"""
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password is successfully updated!')
            return redirect('authentication:logout')
        messages.error(request, 'Please correct the error below.')
        return redirect(request.path_info)
