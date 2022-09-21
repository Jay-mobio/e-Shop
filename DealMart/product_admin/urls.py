from django.urls import path
from product_admin.views import profile,inventory
app_name = 'product_admin'

urlpatterns = [
    path("profile/",profile.ProfileUpdate.as_view(),name="profile"),
    path("remove_profile_image/<int:pk>",profile.RemoveProfileImage.as_view(),name="remove_profile_pic"),
    path('inventory_update/<int:pk>',inventory.UpdateInventory.as_view(),name="inventory"),
    path('inventory/',inventory.InventoryList.as_view(),name="inventory_list")

]