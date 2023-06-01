from django import forms

from product.models import Product


class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']  # '__all__'

    def save(self, commit=True):
        new_product = Product.objects.create(
            name=self.cleaned_data.get('name'),  # 사용자가 입력한 내용을 clean_name()하고 깨끗해진 것 가져오자
            price=self.cleaned_data.get('price'),  # 사용자가 입력한 내용을 clean_price()하고 깨끗해진 것 가져오자
        )
        return new_product
