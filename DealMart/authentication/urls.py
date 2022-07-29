from django.urls import path
from .views import Login_View,register_view

app_name = "authentication"

urlpatterns = [
    path('login/',Login_View.LoginView.as_view(),name = "login"),
    path('register/',register_view.RegisterView.as_view(),name = "register"),
]