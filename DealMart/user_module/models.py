from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.forms import EmailField
from .manager import UserManager
# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []