from django import forms
from products.models import Products

class AddProductForm(forms.ModelForm):
    class Meta:
        model=Products
        fields = ['name','category','price','image','discription']
