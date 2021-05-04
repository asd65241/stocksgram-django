from django.forms import ModelForm
from django import forms
from django.forms.models import inlineformset_factory
from .models import *

class SalesEditForm(ModelForm):
    class Meta:
        model = SalesOrder
        fields = ['status','projected_completed_date','completed_date']


class SalesOrderForm(ModelForm):
    class Meta:
        model = SalesOrder
        exclude = ()

OrderItemFormSet = inlineformset_factory(SalesOrder, Item, form=SalesOrderForm, extra=5)