import django_filters as filters
from products.models import Products

class ProductFilter(filters.FilterSet):

    class Meta:
        model = Products
        fields = ['name', 'price']