from django import forms

class ProductUploadForm(forms.Form):
    file = forms.FileField()

class CustomerUploadForm(forms.Form):
    file = forms.FileField()