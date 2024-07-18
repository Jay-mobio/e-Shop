"""PRODUCTS FILTER"""
import django_filters
from products.models import Inventory

class ProductFilters(django_filters.FilterSet):
    """PRODUCTS FILTER"""
    class Meta:
        """DEFINING MODEL"""
        model = Inventory
        fields = [
            'product__name',
            'product__price',
            'product__category',
        ]
