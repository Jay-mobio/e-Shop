from django.urls import path
from order.views import checkout


appname = 'order'

urlpatterns = [
    path('checkout/',checkout.Checkout.as_view(),name="checkout")
]