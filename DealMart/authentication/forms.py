from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserRegister(UserCreationForm):
    phone = forms.IntegerField(max_value=10)
    address = forms.CharField()
    class Meta:
        model = User
        fields = ["username","password1","email","password2","phone","address"] 