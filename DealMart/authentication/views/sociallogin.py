# from allauth.account.views import SignupView
# from allauth.account.views import ImmediateHttpResponse
# from allauth.account.views import app_settings
# from allauth.account.views import complete_signup
# from django.contrib.auth.models import Group
# from allauth.account.utils import passthrough_next_redirect_url
# from django.urls import reverse
# from django.contrib.sites.shortcuts import get_current_site
# from allauth.account.utils import get_request_param 
# from django.contrib.auth.models import Group

# class MySocialAuth(SignupView):
    
#     def get_context_data(self, **kwargs):
#         ret = super(SignupView, self).get_context_data(**kwargs)
#         form = ret["form"]
#         email = self.request.session.get("account_verified_email")
#         group = Group.objects.get['Customer']
#         if email:
#             print("*********************")
#             user = form.save()
#             user.groups.add(group)
#             email_keys = ["email"]
#             if app_settings.SIGNUP_EMAIL_ENTER_TWICE:
#                 email_keys.append("email2")
#             for email_key in email_keys:
#                 form.fields[email_key].initial = email
#         login_url = passthrough_next_redirect_url(
#             self.request, reverse("account_login"), self.redirect_field_name
#         )
#         redirect_field_name = self.redirect_field_name
#         site = get_current_site(self.request)
#         redirect_field_value = get_request_param(self.request, redirect_field_name)
#         ret.update(
#             {
#                 "login_url": login_url,
#                 "redirect_field_name": redirect_field_name,
#                 "redirect_field_value": redirect_field_value,
#                 "site": site,
#             }
#         )
#         return ret

# account_signup_view = MySocialAuth.as_view()



