from products.models import ProductBrand, ProductCat, Product
from customers.models import Customer
from inventory.models import Warehouse, Stocklevel
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
import shortuuid
import pandas as pd
import os
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, transaction

# Initialize Random ID
shortuuid.set_alphabet("ABCDEFGHIJKLMNOPQRSTUVWXYZ012345678")
# To use radom id, use:
# shortuuid.uuid()[:12]

def handle_customers_file(f):
    file_name = f'upload_pool/{shortuuid.uuid()[:12]}.xlsx'
    with open(file_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    
    df = pd.read_excel(file_name,skiprows=[0,1],keep_default_na=False)
    existed_customer = []
    for index, row in df.iterrows():
        customer, created = Customer.objects.get_or_create(type=row['type*'], name=row['name*'],sex=row['sex*'], phone=row['phone*'],email=row['email'], address=row['address'])
        if created:
            customer.save()
        else:
            existed_customer.append(customer.name)

    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        print('File not exist')

    return existed_customer

def handle_product_file(f):
    file_name = f'upload_pool/{shortuuid.uuid()[:12]}.xlsx'
    with open(file_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    
    df = pd.read_excel(file_name,skiprows=[0,1,2])
    df = df.astype({'price*': float,'cost':float,'stock_unit*':int})

    for index, row in df.iterrows():
        product_cat, _ = ProductCat.objects.get_or_create(name=row['product_cat*'])
        product_cat.save()
        product_brand, _ = ProductBrand.objects.get_or_create(name=row['brand_name*'],other_name=row['brand_other_name'])
        product_brand.save()
        product, _ = Product.objects.get_or_create(barcode=row['product_barcode'],name=row['product_name*'],brand=product_brand,catagory=product_cat)
        product.save()
        warehouse, _ = Warehouse.objects.get_or_create(name=row['warehouse*'],type=row['warehouse_type*'])
        warehouse.save()

        expiry_date = None
        cost = None
        
        if not pd.isnull(row['expiry_date']):
            expiry_date = row['expiry_date']
        if not pd.isnull(row['cost']):
            cost = row['cost']

        print(f"stock_unit: {row['stock_unit*']}, cost: {row['cost']}, price: {row['price*']}")
        stocklevel, _ = Stocklevel.objects.get_or_create(product=product,storage=warehouse,expiry_date=expiry_date,stock_unit=row['stock_unit*'],price=row['price*'],cost=cost,remark=row['stock_remark'])
        stocklevel.save()

    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        print('File not exist')


@login_required
def products_upload(request):
    if request.method == 'POST':
        form = ProductUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                with transaction.atomic():
                    handle_product_file(request.FILES['file'])
                    return redirect(f'/products', messages.success(request, 'Products was successfully added.', 'bg-success'))
            except IntegrityError:
                return redirect('/products', messages.error(request, f'Error: File Error', 'bg-danger'))
        else:
            return redirect(f'/products', messages.error(request, 'File is not valid', 'bg-danger'))
    else:
        form = ProductUploadForm()
    return render(request, 'fileupload/products_upload.html', {'form': form})

@login_required
def customers_upload(request):
    if request.method == 'POST':
        form = CustomerUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                with transaction.atomic():
                    already_exist = handle_customers_file(request.FILES['file'])
                    if already_exist:
                        return redirect(f'/customers', messages.success(request, f'{",".join(already_exist)} already exsisted.', 'bg-success'))
                    else:
                        return redirect(f'/customers', messages.success(request, 'Customers was successfully added.', 'bg-success'))
            except IntegrityError:
                return redirect('/customers', messages.error(request, f'Error: File Error', 'bg-danger'))
        else:
            return redirect(f'/customers', messages.error(request, 'File is not valid', 'bg-danger'))
    else:
        form = CustomerUploadForm()
    return render(request, 'fileupload/customers_upload.html', {'form': form})
