from django.contrib.auth.views import PasswordContextMixin
from django.views.generic import TemplateView
from django.shortcuts import resolve_url
from django.conf import settings


class PasswordResetCompleteView(PasswordContextMixin, TemplateView):
    template_name = "authentication/password_reset_complete.html"
    title = ("Password reset complete")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["login_url"] = resolve_url(settings.LOGIN_URL)
        return context