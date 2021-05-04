from django.forms.fields import DateField
from inventory.models import Stocklevel
from django.shortcuts import render, redirect
from .models import Product, ProductBrand, ProductCat
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.db.models import Count, Sum


@login_required
def index_product(request):
    instance = Product.objects.annotate(
        total_stocks=Sum('product_stock__stock_unit'))
    return render(request, 'products/index_product.html', {'products': instance})

# Cat


@login_required
def index_cat(request):
    instance = ProductCat.objects.annotate(num_products=Count('product_cat'))
    return render(request, 'products/index_cat.html', {'cats': instance})

# Brand


@login_required
def index_brand(request):
    instance = ProductBrand.objects.annotate(
        num_products=Count('product_brand'))
    return render(request, 'products/index_brand.html', {'brands': instance})


@login_required
def detail(request, product_id):
    instance = Product.objects.get(id=product_id)
    return render(request, 'products/product_detail.html', {'product': instance})


@login_required
def product_addstock(request, product_id):
    StockFromSet = inlineformset_factory(Product, Stocklevel, fields=('storage', 'expiry_date', 'stock_unit', 'price', 'cost', 'remark'), extra=5)
    instance = Product.objects.get(id=product_id)
    formset = StockFromSet(queryset=Stocklevel.objects.none(), instance=instance)
    if request.POST:
        formset = StockFromSet(request.POST, instance=instance)
        if formset.is_valid():
            if formset.save():
                return redirect(f'/product/detail/{product_id}/', messages.success(request, 'Product Stock was successfully updated.', 'bg-success'))
            else:
                return redirect(f'/product/detail/{product_id}/', messages.error(request, 'Data is not saved', 'bg-danger'))
        else:
            return redirect(f'/product/detail/{product_id}/', messages.error(request, 'Form is not valid', 'bg-danger'))
    else:
        return render(request, 'products/product_addstock.html', {'product': instance, 'formset': formset})

# Cat Detail


@login_required
def cat_detail(request, cat_id):
    instance = ProductCat.objects.get(id=cat_id)
    return render(request, 'products/cat_detail.html', {'cat': instance})


# Brand Detail
@login_required
def brand_detail(request, brand_id):
    instance = ProductBrand.objects.get(id=brand_id)
    return render(request, 'products/brand_detail.html', {'brand': instance})


@login_required
def edit(request, product_id):
    instance = Product.objects.get(id=product_id)
    if request.POST:
        form = ProductForm(request.POST, instance=instance)
        if form.is_valid():
            if form.save():
                return redirect('/products', messages.success(request, 'Product was successfully updated.', 'bg-success'))
            else:
                return redirect('/products', messages.error(request, 'Data is not saved', 'bg-danger'))
        else:
            return redirect('/products', messages.error(request, 'Form is not valid', 'bg-danger'))
    else:
        form = ProductForm(instance=instance)
        return render(request, 'products/edit_product.html', {'form': form})


@login_required
def edit_cat(request, cat_id):
    instance = ProductCat.objects.get(id=cat_id)
    if request.POST:
        form = ProductCatForm(request.POST, instance=instance)
        if form.is_valid():
            if form.save():
                return redirect('/product/cat', messages.success(request, 'Product was successfully updated.', 'bg-success'))
            else:
                return redirect('/product/cat', messages.error(request, 'Data is not saved', 'bg-danger'))
        else:
            return redirect('/product/cat', messages.error(request, 'Form is not valid', 'bg-danger'))
    else:
        form = ProductCatForm(instance=instance)
        return render(request, 'products/edit_cat.html', {'form': form})

# Brand


@login_required
def edit_brand(request, brand_id):
    instance = ProductBrand.objects.get(id=brand_id)
    if request.POST:
        form = ProductBrandForm(request.POST, instance=instance)
        if form.is_valid():
            if form.save():
                return redirect('/product/brands', messages.success(request, 'Product was successfully updated.', 'bg-success'))
            else:
                return redirect('/product/brands', messages.error(request, 'Data is not saved', 'bg-danger'))
        else:
            return redirect('/product/brands', messages.error(request, 'Form is not valid', 'bg-danger'))
    else:
        form = ProductBrandForm(instance=instance)
        return render(request, 'products/edit_brand.html', {'form': form})


@login_required
def delete_product(request, product_id):
    instance = Product.objects.get(id=product_id)
    name = instance.name
    instance.delete()
    return redirect('/products', messages.success(request, f'{name} was deleted successfully.', 'bg-success'))


@login_required
def delete_cat(request, cat_id):
    instance = ProductCat.objects.get(id=cat_id)
    name = instance.name
    instance.delete()
    return redirect('/product/cats', messages.success(request, f'{name} was deleted successfully.', 'bg-success'))


@login_required
def delete_brand(request, brand_id):
    instance = ProductBrand.objects.get(id=brand_id)
    name = instance.name
    instance.delete()
    return redirect('/product/brands', messages.success(request, f'{name} was deleted successfully.', 'bg-success'))


@login_required
def new(request):
    if request.POST:
        form = ProductForm(request.POST)
        if form.is_valid():
            if form.save():
                print(form.cleaned_data)
                return redirect('/products', messages.success(request, f'Product was successfully created.', 'bg-success'))
            else:
                return redirect('/products', messages.error(request, 'Data is not saved', 'bg-danger'))
        else:
            return redirect('/products', messages.error(request, 'Form is not valid', 'bg-danger'))
    else:
        form = ProductForm()
        return render(request, 'products/new_product.html', {'form': form})


# Product Cat
@login_required
def new_cat(request):
    if request.POST:
        form = ProductCatForm(request.POST)
        if form.is_valid():
            if form.save():
                print(form.cleaned_data)
                return redirect('/product/cats', messages.success(request, f'Product Cat was successfully created.', 'bg-success'))
            else:
                return redirect('/products/cats', messages.error(request, 'Data is not saved', 'bg-danger'))
        else:
            return redirect('/products/cats', messages.error(request, 'Form is not valid', 'bg-danger'))
    else:
        form = ProductCatForm()
        return render(request, 'products/new_cat.html', {'form': form})

# Product Brand


@login_required
def new_brand(request):
    if request.POST:
        form = ProductBrandForm(request.POST)
        if form.is_valid():
            if form.save():
                print(form.cleaned_data)
                return redirect('/products', messages.success(request, f'Product Brand was successfully created.', 'bg-success'))
            else:
                return redirect('/products', messages.error(request, 'Data is not saved', 'bg-danger'))
        else:
            return redirect('/products', messages.error(request, 'Form is not valid', 'bg-danger'))
    else:
        form = ProductBrandForm()
        return render(request, 'products/new_brand.html', {'form': form})
