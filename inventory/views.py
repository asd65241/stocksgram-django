from django.shortcuts import render, redirect
from .models import Stocklevel, Warehouse
from .forms import WarehouseForm, StocklevelForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

@login_required
def index(request):
    instance = Warehouse.objects.annotate(total_stock=Sum('instock_products__stock_unit'))
    return render(request, 'inventory/index.html', {'warehouses': instance})

@login_required
def detail(request, warehouse_id):
    instance = Warehouse.objects.get(id=warehouse_id)
    total_product = instance.instock_products.count()
    total_stock = instance.instock_products.aggregate(Sum('stock_unit'))
    return render(request, 'inventory/detail.html', {'warehouse': instance, 'total_product': total_product, 'total_stock': total_stock})

@login_required
def new(request):
    if request.POST:
        form = WarehouseForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/inventories', messages.success(request, f'Warehouse was successfully created.', 'bg-success'))
            else:
                return redirect('/inventories', messages.error(request, 'Data is not saved', 'bg-danger'))
        else:
            return redirect('/inventories', messages.error(request, 'Form is not valid', 'bg-danger'))
    else:
        form = WarehouseForm()
        return render(request, 'inventory/new.html', {'form':form})

@login_required
def edit(request, warehouse_id):
    instance = Warehouse.objects.get(id=warehouse_id)
    if request.POST:
        form = WarehouseForm(request.POST, instance=instance)
        if form.is_valid():
            if form.save():
                return redirect('/inventories', messages.success(request, 'Warehouse was successfully updated.', 'bg-success'))
            else:
                return redirect('/inventories', messages.error(request, 'Data is not saved', 'bg-danger'))
        else:
            return redirect('/inventories', messages.error(request, 'Form is not valid', 'bg-danger'))
    else:
        form = WarehouseForm(instance=warehouse_id)
        return render(request, 'inventory/edit.html', {'form':form})

@login_required
def delete(request, warehouse_id):
    instance = Warehouse.objects.get(id=warehouse_id)
    name = instance.name
    try:
        instance.delete()
        return redirect('/inventories', messages.success(request, f'Warehouse {name} was successfully deleted.', 'bg-success'))
    except:
        return redirect('/inventories', messages.error(request, f'Cannot delete non empty warehouse', 'bg-danger'))
