from django import forms
from .models import Product


# Define a form class for the Product model
class ProductForm(forms.ModelForm):
    class Meta:
        # Specify the model associated with this form
        model = Product
        # Include all fields of the Product model in the form
        fields = '__all__'
