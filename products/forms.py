from django.forms import ModelForm, inlineformset_factory
from django import forms
from .models import *

class ProductCatForm(ModelForm):
    class Meta:
        model = ProductCat
        fields = ['name']

class ProductBrandForm(ModelForm):
    class Meta:
        model = ProductBrand
        fields = ['name','other_name']

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['barcode','name','brand','catagory']