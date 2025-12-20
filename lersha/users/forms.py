from django.forms import ModelForm
from .models import Farmer
from authentication.models import LershaUser
from market.models import Category

class FarmerUpdateForm(ModelForm):
# Must only try to update the specified fields and not all fields
    class Meta:
        model = Farmer
        fields = ['image', 'phone_number', 'address', 'city']

class FarmerUserUpdateForm(ModelForm):
    class Meta:
        model = LershaUser
        fields = ['first_name', 'last_name', 'email']

from django import forms
from .models import Product  # Adjust the import if Product is in a different app

class ProductForm(forms.ModelForm):
    UNIT_CHOICES = [
        ('item', 'Item'),
        ('kg', 'Kg'),
        ('litre', 'Litre'),
    ]

    quantity_unit = forms.ChoiceField(
        choices=UNIT_CHOICES,
        widget=forms.Select(attrs={
            'class': 'px-4 py-3 border rounded-lg focus:ring-2 focus:ring-green-500 outline-none'
        })
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select Category",
        widget=forms.Select(attrs={
            'class': 'px-4 py-3 border rounded-lg focus:ring-2 focus:ring-green-500 outline-none'
        })
    )

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity_unit', 'quantity_unit', 'category', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'px-4 py-3 border rounded-lg focus:ring-2 focus:ring-green-500 outline-none',
                'placeholder': 'Enter product name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'px-4 py-3 border rounded-lg focus:ring-2 focus:ring-green-500 outline-none resize-none',
                'rows': 4,
                'placeholder': 'Describe your product'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'px-4 py-3 border rounded-lg focus:ring-2 focus:ring-green-500 outline-none',
                'placeholder': 'Enter price'
            }),
            'quantity_unit': forms.NumberInput(attrs={
                'class': 'px-4 py-3 border rounded-lg focus:ring-2 focus:ring-green-500 outline-none',
                'placeholder': 'Enter quantity'
            }),
            'image': forms.FileInput(attrs={
                'class': 'px-4 py-2 border rounded-lg focus:ring-2 focus:ring-green-500 outline-none'
            }),
        }

class ProductUpdateForm(forms.ModelForm):
    """
    Form for creating and editing Product listings by farmers.
    Used in the farmer's product detail view for inline editing.
    """

    class Meta:
        model = Product
        fields = [
            'name',
            'image',
            'price',
            'quantity_unit',
            'stock',
            'description',
            'organic',
            'delivery_available',
        ]

class ProductDeleteForm(forms.Form):
    pass