"""OTP GENERATION PAGE"""
import random
from django.core.mail import send_mail
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.shortcuts import redirect,render
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from user_module.models import User
from authentication.models import UserOTP

class OTP(CreateView):
    """OTP OPERATIONS"""
    def post(self,request):
        """CONFIGURATION OF USER OTP"""
        get_otp = request.POST.get('otp')
        get_usr = request.POST.get('usr')
        usr = User.objects.get(email=get_usr)

        if not get_otp.isdigit():
            messages.error(request,"Valueerror")
            return redirect('authentication:verify_otp')
        if int(get_otp) == UserOTP.objects.filter(user = usr).last().otp:
            usr.is_active = True
            usr.save()
            messages.success(request,'Account is Created For '+ usr.email)
            return redirect('authentication:login')
        messages.error(request,'You Entered a Wrong OTP')
        return render(request, 'authentication/otp.html', {'otp': True, 'usr': usr})

    def generateotp(self,usr):
        """GENERATING OTP"""
        usr_otp = random.randrange(100000,999999,6)
        UserOTP.objects.create(user = usr, otp = usr_otp)
        mess = f"Hello {usr.first_name},\nYour OTP is {usr_otp}\nThanks!"
        send_mail(
            "Welcome DealMart member - Verify Your Email",
            mess,
            settings.EMAIL_HOST_USER,
            [usr.email],
            fail_silently = False
            )

@csrf_exempt
def resend_otp(request):
    """RESEND OTP OPERATION"""
    if request.method == 'POST':
        usr_otp = random.randrange(100000,999999,6)
        user = request.POST.get('usr')
        user = User.objects.get(email = user)
        UserOTP.objects.create(user = user, otp = usr_otp)
        mess = f"Hello {user.first_name},\nYour OTP is {usr_otp}\nThanks!"
        send_mail(
            "Welcome DealMart member - Verify Your Email",
            mess,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently = False
            )
    return JsonResponse({'message':True}, status = 200)
