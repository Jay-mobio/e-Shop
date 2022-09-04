from dataclasses import field
import django_filters
from products.models import Inventory

class ProductFilters(django_filters.FilterSet):

    class Meta:
        model = Inventory
        fields = [
            'product__name',
            'product__price',
            'product__category',
        ]