from django import forms
from products.models import Products
from django.core.exceptions import ValidationError


class AddProductForm(forms.ModelForm):
    class Meta:
        model=Products
        fields = ['name','category','sub_category','brand','price','image','discription']

        def clean_price(self):
            price = self.cleaned_data["price"]
            if price == "":
                raise ValidationError("Price required")
            if not price.isdigit():
                raise ValidationError("Price should be number")
            return price

        def clean_category(self):
            category = self.cleaned_data["price"]
            if category == "":
                raise ValidationError("Category required")  

        def clean_sub_category(self):
            sub_category = self.cleaned_data["price"]
            if sub_category == "":
                raise ValidationError("Size required")
        
        def clean_brand(self):
            price = self.cleaned_data["brand"]
            if price == "":
                raise ValidationError("Brand required")

        def clean_discription(self):
            price = self.cleaned_data["discription"]
            if price == "":
                raise ValidationError("Discription required")
        
        def is_valid(self) -> bool:
            return True

        def clean_image(self):
            image = self.cleaned_data['image']
            if image is None:
                pass
