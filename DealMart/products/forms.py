from django import forms
from products.models import Products
class AddProductForm(forms.ModelForm):
    # sub_category = forms.ChoiceField(required=False, widget=forms.Select())
    class Meta:
        model=Products
        fields = ['name','category','sub_category','brand','price','image','discription']

    def is_valid(self) -> bool:
        return True

    def clean_image(self):
        image = self.cleaned_data['image']
        if image is None:
            pass
