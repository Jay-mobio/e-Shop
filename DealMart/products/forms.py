"""PRODUCTS APP FORMS"""
from django import forms
from django.core.exceptions import ValidationError
from products.models import Products


class AddProductForm(forms.ModelForm):
    """ADD PRODUCT FORM"""
    class Meta:
        """DEFINING MODEL IN FORM"""
        model=Products
        fields = ['name','category','sub_category','brand','price','image','discription']

        def clean_price(self):
            """PRICE VALIDATION"""
            price = self.cleaned_data["price"]
            if price == "":
                raise ValidationError("Price required")
            if not price.isdigit():
                raise ValidationError("Price should be number")
            return price

        def clean_category(self):
            """CATEGORY VALIDATION"""
            category = self.cleaned_data["price"]
            if category == "":
                raise ValidationError("Category required")

        def clean_sub_category(self):
            """SUBCATEGORY VALIDATION"""
            sub_category = self.cleaned_data["price"]
            if sub_category == "":
                raise ValidationError("Size required")

        def clean_brand(self):
            """BRAND VALIDATION"""
            price = self.cleaned_data["brand"]
            if price == "":
                raise ValidationError("Brand required")

        def clean_discription(self):
            """DISCRIPTION VALIDATION"""
            price = self.cleaned_data["discription"]
            if price == "":
                raise ValidationError("Discription required")

        def is_valid(self) -> bool:
            """FORM VALIDATION"""
            return True

        def clean_image(self):
            """IMAGE VALIDATION"""
            image = self.cleaned_data['image']
            if image is None:
                pass
