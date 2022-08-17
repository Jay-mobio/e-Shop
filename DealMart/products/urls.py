from django.urls import path
from products.views import add_product

app_name = 'products'

urlpatterns = [
    path('add_product/',add_product.AddProduct.as_view(),name="add_product")
]
