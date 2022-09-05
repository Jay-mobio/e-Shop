from django.urls import path
from customer.views import customer_profile

    
app_name = 'customer'

urlpatterns = [
    path("customer_profile/<int:pk>",customer_profile.CustomerProfileUpdate.as_view(),name="customer_profile"),
   path("customer_remove_profile_image/<int:pk>",customer_profile.CustomerRemoveProfileImage.as_view(),name="customer_remove_profile_pic")

]