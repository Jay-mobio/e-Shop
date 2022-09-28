"""LOGOUT"""
from django.contrib.auth import logout
from django.conf import settings
from django.views import View
from django.shortcuts import redirect


class LogoutView(View):
    """LOGOUT OPERATIONS"""
    def get(self, request):
        """LOGGING OUT USER"""
        logout(request)
        return redirect(settings.LOGIN_URL)
