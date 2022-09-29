"""ADD INVENTORY FORMS"""
from django import forms
from products.models import Inventory
# from django.contrib.auth.forms import ModelForm


class AddInventoryForm(forms.ModelForm):
    """ADD INVENTORY FORM"""
    class Meta:
        """MODEL DEFINING IN FORM"""
        model = Inventory
        fields = ('product','product_quantity','is_active','created_by')
