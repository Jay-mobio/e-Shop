from authentication.models import UserOTP
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.views import View
from django.views.generic.edit import CreateView
from user_module.models import User
from django.contrib import messages
from django.shortcuts import redirect,render
import random
from django.conf import settings

class OTP(CreateView):
	def post(self,request):
		get_otp = request.POST.get('otp')
		if get_otp:
			get_usr = request.POST.get('usr')
			usr = User.objects.get(email=get_usr)
			if int(get_otp) == UserOTP.objects.filter(user = usr).last().otp:
				usr.is_active = True
				usr.save()
				messages.success(request, f'Account is Created For '+ usr.email)
				return redirect('authentication:login')
			else:
				messages.warning(request, f'You Entered a Wrong OTP')
				return render(request, 'authentication/otp.html', {'otp': True, 'usr': usr})
		

	def generateotp(self,request,usr):
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
			

		

class ResendOTP(View):

	def post(self, request):
		get_usr = request.POST.get('usr', None)
		# print(get_usr)
		if User.objects.filter(email = get_usr).exists() and not User.objects.get(email = get_usr).is_active:
			usr = User.objects.get(email=get_usr)
			usr_otp = random.randrange(100000,999999,6)
			UserOTP.objects.create(user = usr, otp = usr_otp)
			mess = f"Hello {usr.first_name},\nYour OTP is {usr_otp}\nThanks!"

			send_mail(
				"Welcome to DealMart - Verify Your Email",
				mess,
				settings.EMAIL_HOST_USER,
				[usr.email],
				fail_silently = False
				)
			return HttpResponse("Resend")

		return JsonResponse({"success": True})