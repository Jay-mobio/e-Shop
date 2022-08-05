from django.contrib.auth.views import *
from django.views.generic.edit import FormView
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.utils.http import urlsafe_base64_decode
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login
from user_module.models import User


# class PasswordResetConfirmView(PasswordContextMixin, FormView):
#     form_class = SetPasswordForm
#     post_reset_login = False
#     post_reset_login_backend = None
#     reset_url_token = "set-password"
#     success_url = "/reset_password_complete/"
#     template_name = "authentication/password_reset_form.html"
#     title = ("Enter new password")
#     token_generator = default_token_generator
#     def get_context_data(self,**kwargs):
#         context = super(PasswordResetConfirmView,self).get_context_data(**kwargs)
#         if self.validlink:
#             context["validlink"] = True
#         else:
#             context.update(
#                 {
#                     "form": None,
#                     "title": ("Password reset unsuccessful"),
#                     "validlink": False,
#                 }
#             )
#         return context

class PasswordResetConfirmView(PasswordContextMixin, FormView):
    form_class = SetPasswordForm
    post_reset_login = False
    post_reset_login_backend = None
    reset_url_token = 'set-password'
    success_url = '/reset_password_complete/'
    template_name = "authentication/password_reset_form.html"
    title = ('Enter new password')
    token_generator = default_token_generator
    @method_decorator(sensitive_post_parameters())
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        if 'uidb64' not in kwargs or 'token' not in kwargs:
            raise ImproperlyConfigured(
                "The URL path must contain 'uidb64' and 'token' parameters."
            )
        self.validlink = False
        self.user = self.get_user(kwargs['uidb64'])
        if self.user is not None:
            token = kwargs['token']
            if token == self.reset_url_token:
                session_token = self.request.session.get(INTERNAL_RESET_SESSION_TOKEN)
                if self.token_generator.check_token(self.user, session_token):
                    # If the token is valid, display the password reset form.
                    self.validlink = True
                    return super().dispatch(*args, **kwargs)
            else:
                if self.token_generator.check_token(self.user, token):
                    # Store the token in the session and redirect to the
                    # password reset form at a URL without the token. That
                    # avoids the possibility of leaking the token in the
                    # HTTP Referer header.
                    self.request.session[INTERNAL_RESET_SESSION_TOKEN] = token
                    redirect_url = self.request.path.replace(token, self.reset_url_token)
                    return HttpResponseRedirect(redirect_url)
        # Display the "Password reset unsuccessful" page.
        return self.render_to_response(self.get_context_data())
    def get_user(self, uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist, ValidationError):
            user = None
        return user
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.user
        return kwargs
    def form_valid(self, form):
        user = form.save()
        del self.request.session[INTERNAL_RESET_SESSION_TOKEN]
        if self.post_reset_login:
            auth_login(self.request, user, self.post_reset_login_backend)
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.validlink:
            context['validlink'] = True
        else:
            context.update({
                'form': None,
                'title': ('Password reset unsuccessful'),
                'validlink': False,
            })
        return context

