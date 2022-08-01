from django.urls import path
from .views import login_View,register_view

app_name = "authentication"

urlpatterns = [
    path('login/',login_View.LoginView.as_view(),name = "login"),
    path('register/',register_view.RegisterView.as_view(),name = "register"),
]