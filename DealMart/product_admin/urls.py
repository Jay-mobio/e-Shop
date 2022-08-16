from django.urls import path
from product_admin.views import home
app_name = 'product_admin'

urlpatterns = [
    path('home/',home.HomeView.as_view(),name='home'),
]