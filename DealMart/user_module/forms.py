from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "phone", "password1", "password2")

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        try:
            if int(phone) > 9:
                return phone
            else:
                raise forms.ValidationError("phone number seems incorrect !!!")
        except ValueError:
            raise forms.ValidationError("phone number must be NUMBER !!!")
