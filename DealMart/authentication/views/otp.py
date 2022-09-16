from authentication.models import UserOTP
from django.core.mail import send_mail
from django.views.generic.edit import CreateView
from user_module.models import User
from django.contrib import messages
from django.shortcuts import redirect,render
import random
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

class OTP(CreateView):
	def post(self,request):
		get_otp = request.POST.get('otp')
		get_usr = request.POST.get('usr')
		usr = User.objects.get(email=get_usr)
		try :
			if int(get_otp) == UserOTP.objects.filter(user = usr).last().otp:
				usr.is_active = True
				usr.save()
				messages.success(request, f'Account is Created For '+ usr.email)
				return redirect('authentication:login')
			else:
				messages.error(request, f'You Entered a Wrong OTP')
				return render(request, 'authentication/otp.html', {'otp': True, 'usr': usr})
		except ValueError :
			return redirect("authentication:verify_otp")

		

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
			

		

@csrf_exempt
def resend_otp(request):
	if request.method == 'POST':
		usr_otp = random.randrange(100000,999999,6)
		user = request.POST.get('usr')
		user = User.objects.get(email = user)
		usr = UserOTP.objects.create(user = user, otp = usr_otp)
		mess = f"Hello {user.first_name},\nYour OTP is {usr_otp}\nThanks!"
		send_mail(
			"Welcome DealMart member - Verify Your Email",
			mess,
			settings.EMAIL_HOST_USER,
			[user.email],
			fail_silently = False
			)
	return JsonResponse({'message':True}, status = 200)
		
