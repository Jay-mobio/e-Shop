from django.urls import path
from products.views import products,dashboard,update_product,delete_product
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'

urlpatterns = [
    path('dashboard/',dashboard.Dashboard.as_view(),name="dashboard"),
    path('add_product/',products.AddProduct.as_view(),name="add_product"),
    path('update_product/<int:pk>/',update_product.UpdateProduct.as_view(),name="update_product"),
    path('delete_product/<int:pk>',delete_product.DeleteProduct.as_view(),name="delete_product"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)