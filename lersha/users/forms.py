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
        ('Item', 'Item'),
        ('KG', 'KG'),
        ('Litre', 'Litre'),
    ]

    quantity_unit = forms.ChoiceField(
        choices=UNIT_CHOICES,
        widget=forms.Select(attrs={
            'class': 'px-4 py-3 border rounded-lg focus:ring-2 focus:ring-green-500 outline-none'
        })
    )

    stock = forms.FloatField(
        widget=forms.NumberInput(attrs={
            'class': 'px-4 py-3 border rounded-lg focus:ring-2 focus:ring-green-500 outline-none',
            'placeholder': 'Enter stock'
        })
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select Category",
        widget=forms.Select(attrs={
            'class': 'px-4 py-3 border rounded-lg focus:ring-2 focus:ring-green-500 outline-none'
        })
    )

    organic = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'w-5 h-5 text-primary-600 border-primary-300 rounded focus:ring-primary-500 cursor-pointer transition-colors'
        })
    )

    delivery_available = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'w-5 h-5 text-primary-600 border-primary-300 rounded focus:ring-primary-500 cursor-pointer transition-colors'
        })
    )
    

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity_unit', 'quantity_unit', 'category', 'image', 'stock']
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
            'stock': forms.NumberInput(attrs={
                'class': 'px-4 py-3 border rounded-lg focus:ring-2 focus:ring-green-500 outline-none',
                'placeholder': 'Enter stock'
            }),
            'quantity_unit': forms.NumberInput(attrs={
                'class': 'px-4 py-3 border rounded-lg focus:ring-2 focus:ring-green-500 outline-none',
                'placeholder': 'Enter quantity'
            }),
            'delivery_available': forms.CheckboxInput(attrs={
                'class': 'w-5 h-5 text-primary-600 border-primary-300 rounded focus:ring-primary-500 cursor-pointer transition-colors'
            }),
            'organic': forms.CheckboxInput(attrs={
                'class': 'w-5 h-5 text-primary-600 border-primary-300 rounded focus:ring-primary-500 cursor-pointer transition-colors'
            }),
            'category': forms.Select(attrs={
                'class': 'px-4 py-3 border rounded-lg focus:ring-2 focus:ring-green-500 outline-none'
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
            'category',
            'organic',
            'delivery_available',
        ]

class ProductDeleteForm(forms.Form):
    pass