from django.core.exceptions import ValidationError
from products.models import Inventory
from django import forms
# from django.contrib.auth.forms import ModelForm


class AddInventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ('product','product_quantity','is_active','created_by')