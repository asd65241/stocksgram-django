from django.contrib.messages.api import error, success
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.db import IntegrityError, transaction


@login_required
def index(request):
    instance = SalesOrder.objects.all()
    return render(request, 'orders/index.html', {'orders': instance})


@login_required
def sales_detail(request, order_id):
    instance = SalesOrder.objects.get(id=order_id)
    item_total = instance.order_items.aggregate(Sum('total_amount'))
    return render(request, 'orders/detail.html', {'order': instance, 'item_total': item_total})


@login_required
@transaction.atomic
def sales_new(request):
    if request.POST:
        form = SalesOrderForm(request.POST)
        if form.is_valid():
            errorItem = []
            try:
                with transaction.atomic():
                    savedObj = form.save()
                    if savedObj:
                        items = OrderItemFormSet(
                            request.POST, instance=savedObj)
                        if items.is_valid():
                            savedItems = items.save()
                            for item in savedItems:
                                order_quantity = item.quantity
                                # Decrement Stock Count
                                slevel = Stocklevel.objects.get(
                                    id=item.product.id)
                                slevel.stock_unit -= order_quantity
                                if slevel.stock_unit < 0:
                                    errorItem.append(item.product.product.name)
                                else:
                                    slevel.save()
                            if errorItem:
                                raise IntegrityError
                            else:
                                savedObj.save()
                                return redirect('/orders', messages.success(request, 'Order was successfully created.', 'bg-success'))
            except IntegrityError:
                return redirect('/orders', messages.error(request, f'Out of stock: {",".join(errorItem)}', 'bg-danger'))
        else:
            return redirect('/orders', messages.error(request, 'Form is not valid', 'bg-danger'))
    else:
        form = SalesOrderForm()
        items = OrderItemFormSet()
        return render(request, 'orders/new.html', {'form': form, 'items': items})


@login_required
def sales_edit(request, order_id):
    instance = SalesOrder.objects.get(id=order_id)
    if request.POST:
        form = SalesEditForm(request.POST, instance=instance)
        if form.is_valid():
            if form.save():
                return redirect('/orders', messages.success(request, 'Order was successfully updated.', 'bg-success'))
            else:
                return redirect('/orders', messages.error(request, 'Data is not saved', 'bg-danger'))
        else:
            return redirect('/orders', messages.error(request, 'Form is not valid', 'bg-danger'))
    else:
        form = SalesEditForm(instance=instance)
        return render(request, 'orders/edit.html', {'form': form, 'order':instance})


@login_required
def sales_destroy(request, order_id):
    instance = SalesOrder.objects.get(id=order_id)
    instance.delete()
    return redirect('/orders', messages.success(request, 'Order was successfully deleted.', 'bg-success'))
