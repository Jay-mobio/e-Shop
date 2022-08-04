from django import forms

from user_module.models import User
from django.contrib.auth.forms import PasswordChangeForm



class CustomPwdChgForm(PasswordChangeForm):
    Old_Password = forms.CharField
    New_Password = forms.CharField
    New_Password = forms.CharField

    class meta:
        model = User

