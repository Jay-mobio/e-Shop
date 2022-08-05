from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import resolve_url
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.views.generic import RedirectView


class LogoutView(RedirectView):

    next_page = None
    redirect_field_name = "authentication/login.html"
    template_name = "authentication/customer_login_page.html"
    extra_context = None

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        next_page = self.get_next_page()
        if next_page:
            # Redirect to this page until the session has been cleared.
            return HttpResponseRedirect(next_page)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Logout may be done via POST."""
        return self.get(request, *args, **kwargs)

    def get_next_page(self):
        if self.next_page is not None:
            next_page = resolve_url(self.next_page)
        elif settings.LOGOUT_REDIRECT_URL:
            next_page = resolve_url(settings.LOGOUT_REDIRECT_URL)
        else:
            next_page = self.next_page

        if (
            self.redirect_field_name in self.request.POST
            or self.redirect_field_name in self.request.GET
        ):
            next_page = self.request.POST.get(
                self.redirect_field_name, self.request.GET.get(self.redirect_field_name)
            )
            url_is_safe = url_has_allowed_host_and_scheme(
                url=next_page,
                allowed_hosts=self.get_success_url_allowed_hosts(),
                require_https=self.request.is_secure(),
            )
            # Security check -- Ensure the user-originating redirection URL is
            # safe.
            if not url_is_safe:
                next_page = self.request.path
        return next_page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        context.update(
            {
                "site": current_site,
                "site_name": current_site.name,
                "title": ("Logged out"),
                **(self.extra_context or {}),
            }
        )
        return context