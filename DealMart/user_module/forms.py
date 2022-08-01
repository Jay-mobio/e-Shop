from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)
