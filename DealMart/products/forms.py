from django import forms
from products.models import Products

class AddProductForm(forms.ModelForm):
    class Meta:
        model=Products
        fields = ['name','category','sub_category','price','image','discription']
