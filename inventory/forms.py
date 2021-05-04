from django.forms import ModelForm
from django import forms
from .models import Warehouse, Stocklevel

class WarehouseForm(ModelForm):
    class Meta:
        model = Warehouse
        fields = ['type','name']

class StocklevelForm(ModelForm):
    class Meta:
        model = Stocklevel
        fields = ['product','storage','expiry_date','stock_unit','price','cost','remark']