from django.urls import path
from order.views import checkout,order,orderhistory


app_name = 'order'

urlpatterns = [
    path('checkout/',checkout.Checkout.as_view(),name="checkout"),
    path('orderplaced/',order.CreateOrder.as_view(),name="create_order"),
    path('order_placed/',order.OrderPlaced.as_view(),name="order_placed"),
    path('order_history/',orderhistory.OrderHistory.as_view(),name="orderhistory")
]