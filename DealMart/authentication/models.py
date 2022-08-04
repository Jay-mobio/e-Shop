from django.db import models
from user_module.models import User

class UserOTP(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    time_st = models.DateTimeField(auto_now=True)
    otp = models.IntegerField()