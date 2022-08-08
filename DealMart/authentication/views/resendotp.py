from user_module.models import User
from authentication.models import UserOTP
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.views import View
import random
from django.conf import settings

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