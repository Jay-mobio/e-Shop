from django.urls import path
from .views import (
    login_View,register_view,resendotp_view,home_view,
    change_password_view
)


app_name = "authentication"

urlpatterns = [
    path('login/',login_View.CustomLoginView.as_view(),name = "login"),
    path('register/',register_view.RegisterView.as_view(),name = "register"),
    path('resendOTP/',resendotp_view.ResendOTP.as_view(),name='resendOTP'),
    path('home/',home_view.HomeView.as_view(),name='home'),
    path('change_password/',change_password_view.ChangePasswordView.as_view(),name="change_password")
]