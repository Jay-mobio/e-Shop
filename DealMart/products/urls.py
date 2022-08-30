from django.urls import path
from products.views import products,dashboard,update_product,delete_product,subcategory,productdetail
from django.conf import settings
from django.conf.urls.static import static


app_name = 'products'

urlpatterns = [
    path('dashboard/',dashboard.Dashboard.as_view(),name="dashboard"),
    path('add_product/',products.AddProduct.as_view(),name="add_product"),
    path('update_product_form/<int:pk>/',update_product.UpdateForm.as_view(),name="update_product_form"),
    path('product_detail/<int:pk>/',productdetail.ProductDetail.as_view(),name="product_detail"),
    path('delete_product/<int:pk>/',delete_product.DeleteProduct.as_view(),name="delete_product"),
    path('remove_image/<int:pk>/',update_product.RemoveProductImage.as_view(),name="remove_image"),
    path('select_cat/<id>/',subcategory.ChooseSubCategory.as_view(),name="products_sub_categories")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)