from django.contrib.auth import logout
from django.conf import settings
from django.views import View
from django.shortcuts import redirect


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(settings.LOGIN_URL)