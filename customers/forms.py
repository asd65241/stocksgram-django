from django.forms import ModelForm
from django import forms
from .models import Customer

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['type','name','sex','phone','email','address']