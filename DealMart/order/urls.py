"""ORDER APP URLS"""
from django.urls import path
from order.views import checkout,order,orderhistory,current_orders,delivered_orders,view_order


app_name = 'order'

urlpatterns = [
    path('checkout/',checkout.Checkout.as_view(),name="checkout"),
    path('orderplaced/',order.CreateOrder.as_view(),name="create_order"),
    path('order_placed/',order.OrderPlaced.as_view(),name="order_placed"),
    path('order_history/',orderhistory.OrderHistory.as_view(),name="orderhistory"),
    path('current_order',current_orders.CurrentOrders.as_view(),name="current_order"),
    path('status_change/<int:pk>',current_orders.OrderStatusUpdate.as_view(),name="status_change"),
    path('delivered_orders/',delivered_orders.DeliveredOrder.as_view(),name="delivered_orders"),
    path('view_order/<int:pk>',view_order.ViewOrder.as_view(),name="view_order"),
]
