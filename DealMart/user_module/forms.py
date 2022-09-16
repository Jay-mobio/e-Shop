from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import User
from django.contrib.auth.forms import PasswordResetForm

class UserRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','phone','password1','password2')
    
    # def is_valid(self) -> bool:
    #     return True

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if first_name == "":
            raise ValidationError("First name is required!")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if last_name == "":
            raise ValidationError('Last name is required!')
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
        password1 = self.cleaned_data['password1']
        self.min_length = 1
        # special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
        if len(password1) < 8:
            raise ValidationError("Password too short")
        if not any(char.isdigit() for char in password1):
            raise ValidationError(('Password must contain at least %(min_length)d digit.') % {'min_length': self.min_length})
        if not any(char.isalpha() for char in password1):
            raise ValidationError(('Password must contain at least %(min_length)d letter.') % {'min_length': self.min_length})
        # if not any(char in special_characters for char in password1):
        #     raise ValidationError(('Password must contain at least %(min_length)d special character.') % {'min_length': self.min_length})
        return password1


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password2=="":
            raise ValidationError("Confirm password is required")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2


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
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if last_name == "":
            raise ValidationError('Last name is required!')
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