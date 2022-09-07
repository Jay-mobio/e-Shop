from django.urls import path
from customer.views import customer_profile,cart

    
app_name = 'customer'

urlpatterns = [
    path("customer_profile/<int:pk>",customer_profile.CustomerProfileUpdate.as_view(),name="customer_profile"),
    path("customer_remove_profile_image/<int:pk>",customer_profile.CustomerRemoveProfileImage.as_view(),name="customer_remove_profile_pic"),
    path('add_to_cart/<id>/', cart.addtocart, name="addtocart"),
    path('cart/',cart.ListCart.as_view(),name="cart"),
    path('remove_cart_item/<int:pk>',cart.RemoveCartProduct.as_view(),name="remove_item"),

]