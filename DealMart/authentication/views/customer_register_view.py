from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.contrib import messages
from user_module.forms import UserRegister
from user_module.models import User
from authentication.models import UserOTP
from django.core.mail import send_mail
import random
from django.conf import settings
from django.contrib.auth.models import Group




class CustomerRegisterView(CreateView):
    title = ("Register Page")
    template_name = 'authentication/register_page.html'
    form_class = UserRegister
    
    def post(self,request):
        get_otp = request.POST.get('otp')
        if get_otp:
            get_usr = request.POST.get('usr')
            usr = User.objects.get(email=get_usr)
            if int(get_otp) == UserOTP.objects.filter(user = usr).last().otp:
                usr.is_active = True
                usr.save()
                messages.error(request, 'Account is Created For '+ usr.email)
                return redirect('authentication:login')
            else:
                messages.warning(request,'You Entered a Wrong OTP')
                return render(request, 'authentication/register_page.html', {'otp': True, 'usr': usr})


        form = UserRegister(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            
            if User.objects.filter(email=email).exists():
                messages.success(request,"User already exists")
                return redirect("authentication:register")
            else:
                form.save()
                usr = User.objects.get(email=email)
                group = Group.objects.get(name='Customer')
                usr.groups.add(group)
                usr.is_active = False
                usr.save()
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

                return render(request, 'authentication/register_page.html', {'otp': True, 'usr': usr})

        context = {'form':form}
        return render(request,'authentication/register_page.html',context)