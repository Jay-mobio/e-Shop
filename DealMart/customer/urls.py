"""CUSTOMER APP URLS"""
from customer.views import customer_profile,cart,view_product,update_cart
from django.urls import path

app_name = 'customer'

urlpatterns = [
    path("customer_profile/",customer_profile.CustomerProfileUpdate.as_view(),name="customer_profile"),
    path("customer_remove_profile_image/<int:pk>",customer_profile.CustomerRemoveProfileImage.as_view(),name="customer_remove_profile_pic"),
    path('product_view/<int:pk>/',view_product.ProductView.as_view(),name="product_view"),
    path('cart/',cart.ListCart.as_view(),name="cart"),
    path('update_cart/<int:pk>/',update_cart.UpdateCart.as_view(),name="update_cart"),
    path('remove_cart_item/<int:pk>',cart.RemoveCartProduct.as_view(),name="remove_item"),

]
