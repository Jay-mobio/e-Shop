from django.contrib import messages
from django.contrib.auth.views import PasswordContextMixin
from django.shortcuts import render
from django.views.generic import TemplateView

class PasswordChangeDoneView(PasswordContextMixin, TemplateView):
    template_name = "authentication/login.html"
    title = ("Password change successful")

