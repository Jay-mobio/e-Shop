from django.urls import path
from authentication.views import (
    change_password, login, logout, otp, password_reset,
     register,home
)


app_name = "authentication"

urlpatterns = [
    path('home/',home.HomeView.as_view(),name="home"),
    path('login/',login.LoginView.as_view(),name = "login"),
    path('register/',register.CustomerRegisterView.as_view(),name = "register"),
    path('otp_verify/',otp.OTP.as_view(),name="verify_otp"),
    path('resend_otp/',otp.resend_otp,name = "resend_otp"),
    path('change_password/',change_password.ChangePasswordView.as_view(),name="change_password"),
    path('product_owner_register/',register.ProductAdminRegisterView.as_view(),name='product_admin_register'),
    path('reset_password/',password_reset.ResetPasswordViews.as_view(),name="reset_password"),
    path('password_reset/sent/',password_reset.PasswordChangeDoneView.as_view(),name='reset_password_done'),

    path('reset/<uidb64>/<token>/',password_reset.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),

    path('reset_password_complete/',password_reset.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path('logout/',logout.LogoutView.as_view(),name="logout"),
]
