from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    profile_pic = models.ImageField(null=True, blank = True,default="/static/images/profile1.png")
    address = models.TextField()

    is_email_varified = models.BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
