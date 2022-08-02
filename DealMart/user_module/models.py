from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10,null = True)
    profile_pic = models.ImageField(null=True, blank = True,default="profile1.jpg")
    address = models.TextField()

    is_email_varified = models.BooleanField(Default=False)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []