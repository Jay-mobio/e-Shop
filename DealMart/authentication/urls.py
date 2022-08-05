from django.urls import path
from .views import (
    customer_login_View, customer_register_view, product_admin_register_view,resendotp_view,home_view,
    change_password_view,product_owner_login_view,password_reset_views,password_change_done,
    password_complete_views,password_confirm_views,logout_view,customer_view
)


app_name = "authentication"

urlpatterns = [
    path('login/',customer_login_View.CustomerLoginView.as_view(),name = "login"),
    path('register/',customer_register_view.CustomerRegisterView.as_view(),name = "register"),
    path('resendOTP/',resendotp_view.ResendOTP.as_view(),name='resendOTP'),
    path('home/',home_view.HomeView.as_view(),name='home'),
    path('cuatomer_page/',customer_view.CustomerView.as_view(),name='customer_page'),
    path('change_password/',change_password_view.ChangePasswordView.as_view(),name="change_password"),
    path('product_owner_register/',product_admin_register_view.ProductAdminView.as_view(),name='product_admin_register'),
    path('product_owner_login/',product_owner_login_view.ProductOwnerLoginView.as_view(),name="product_owner_login"),
    path('reset_password/',password_reset_views.ResetPasswordViews.as_view(),name="reset_password"),
    path('password_reset/sent/',password_change_done.PasswordChangeDoneView.as_view(),name='reset_password_done'),

    path('reset/<uidb64>/<token>/',password_confirm_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),

    path('reset_password_complete/',password_complete_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path('logout/',logout_view.LogoutView.as_view(),name="logout")
]