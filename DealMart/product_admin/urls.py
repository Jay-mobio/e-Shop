from django.urls import path
from product_admin.views import profile
app_name = 'product_admin'

urlpatterns = [
<<<<<<< HEAD
    path("profile/<int:pk>",profile.ProfileUpdate.as_view(),name="profile"),
    path("remove_profile_image/<int:pk>",profile.RemoveProfileImage.as_view(),name="remove_profile_pic")
=======
    path("profile/",profile.ProfileUpdate.as_view(),name="profile"),
   path("remove_profile_image/<int:pk>",profile.RemoveProfileImage.as_view(),name="remove_profile_pic")
>>>>>>> feature/customer

]