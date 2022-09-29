"""USER FORMS"""
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordResetForm
from django import forms
from .models import User

class UserRegister(UserCreationForm):
    """USER REGISTER FORM"""
    class Meta:
        """MODEL DEFINIGN"""
        model = User
        fields = ('first_name','last_name','email','phone','password1','password2')


    def clean_first_name(self):
        """FIRST NAME VALIDATION"""
        first_name = self.cleaned_data['first_name']

        if not first_name.isalpha():
            raise ValidationError("Invalid First name!")
        return first_name

    def clean_last_name(self):
        """LAST NAME VALIDATION"""
        last_name = self.cleaned_data['last_name']

        if not last_name.isalpha():
            raise ValidationError("Invalid Last name!")
        return last_name

    def clean_phone(self):
        """PHONE NUMBER VALIDATION"""
        phone = self.cleaned_data['phone']

        if len(phone) < 10 :
            raise ValidationError('Phone number must have atleast 10 digits')
        return phone

    def is_valid(self) -> bool:
        """FORM VALIDATION"""
        return True


class ForgotPassword(PasswordResetForm):
    """FORGOT PASSWOR FORM"""
    def clean_email(self):
        """EMAIL VALIDATION"""
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            raise ValidationError("There is no user registered with the specified email address!")

        return email

class RegisterUser(UserCreationForm):
    """USER REGISTER FORM"""
    class Meta:
        """MODEL DEFINING"""
        model = User
        fields = ('first_name','last_name','email','phone','password1','password2')


    def clean_first_name(self):
        """FIRST NAME VALIDATION"""
        first_name = self.cleaned_data['first_name']
        if first_name == "":
            raise ValidationError("First name is required!")
        if not first_name.isalpha():
            raise ValidationError("Invalid First name!")
        return first_name

    def clean_last_name(self):
        """LAST NAME VALIDATION"""
        last_name = self.cleaned_data['last_name']
        if last_name == "":
            raise ValidationError('Last name is required!')
        if not last_name.isalpha():
            raise ValidationError("Invalid Last name!")
        return last_name

    def clean_email(self):
        """EMIAL VALIDATION"""
        email = self.cleaned_data['email']
        if email == "":
            raise ValidationError('Email is required')
        return email
    def clean_phone(self):
        """PHONE VALIDATION"""
        phone = self.cleaned_data['phone']
        if phone == "":
            raise ValidationError('Phone is required')
        if not phone.isdigit():
            raise ValidationError('Please Enter Valid Mobile Number')
        if len(phone) < 10 :
            raise ValidationError('Phone not valid')
        return phone

    def clean_password1(self):
        """PASSWORD VALIDATION"""
        password1 = self.cleaned_data["password1"]
        if password1 == "":
            raise forms.ValidationError("Password required")
        return password1
    