from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordResetForm
from .models import User
from django import forms

class UserRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','phone','password1','password2')
    

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']

        if not first_name.isalpha():
            raise ValidationError("Invalid First name!")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']

        if not last_name.isalpha():
            raise ValidationError("Invalid Last name!")
        return last_name

    def clean_phone(self):
        phone = self.cleaned_data['phone']

        if len(phone) < 10 :
            raise ValidationError('Phone number must have atleast 10 digits')
        return phone

    def is_valid(self) -> bool:
        return True


class ForgotPassword(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            raise ValidationError("There is no user registered with the specified email address!")

        return email

class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','phone','password1','password2')
    

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if first_name == "":
            raise ValidationError("First name is required!")
        if not first_name.isalpha():
            raise ValidationError("Invalid First name!")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if last_name == "":
            raise ValidationError('Last name is required!')
        if not last_name.isalpha():
            raise ValidationError("Invalid Last name!")
        return last_name

    def clean_email(self):
          email = self.cleaned_data['email']
          if email == "":
              raise ValidationError('Email is required')
          return email
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone == "":
            raise ValidationError('Phone is required')
        if not phone.isdigit():
            raise ValidationError('Please Enter Valid Mobile Number')
        if len(phone) < 10 :
            raise ValidationError('Phone not valid')
        return phone

    def clean_password1(self):
        password1 = self.cleaned_data["password1"]
        if password1 == "":
            raise forms.ValidationError("Password required")
        return password1
    