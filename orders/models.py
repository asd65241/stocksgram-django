from django.db import models
from django.db.models import Sum
from django.db.models.deletion import CASCADE

import datetime
import shortuuid

from inventory.models import *
from customers.models import *
from products.models import *

# Initialize Random ID
shortuuid.set_alphabet("ABCDEFGHIJKLMNOPQRSTUVWXYZ012345678")
# To use radom id, use:
# shortuuid.uuid()[:12]

class SalesChannel(models.Model):
    TYPE = [('B2B', 'B2B'), ('Online', 'Online'), ('Offline', 'Offline')]
    type = models.CharField(max_length=10, choices=TYPE, default='Online')
    name = models.CharField(max_length=64)

    def __str__(self):
        output = f"{self.name} - {self.type}"
        return output


class PaymemtOption(models.Model):
    name = models.CharField(max_length=200)
    services_charge = models.DecimalField(
        default=0, max_digits=8, decimal_places=2)

    def __str__(self):
        output = f"{self.name} (charge: {self.services_charge}%)"
        return output


class Order_ABSTRACT(models.Model):
    STATUS = [('Pending', 'Pending'), ('Completed', 'Completed'),
              ('Outstanding', 'Outstanding'), ('Cancel', 'Cancel')]
    order_id = models.CharField(
        max_length=16, default=f"ORD-{shortuuid.uuid()[:12]}", unique=True, editable=False)
    status = models.CharField(default='Pending', max_length=32, choices=STATUS)
    create_datetime = models.DateField(auto_now=False, auto_now_add=True)
    projected_completed_date = models.DateField(
        default=(datetime.datetime.today() + datetime.timedelta(days=7)))
    completed_date = models.DateField(null=True, blank=True)
    total_amount = models.DecimalField(
        max_digits=12, editable=False, decimal_places=2, default=0)
    total_quantity = models.PositiveIntegerField(default=0, editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.status == 'Completed':
            self.completed_date = datetime.datetime.today()
        if self.status == 'Pending' and datetime.date.today() > self.projected_completed_date:
            self.status =  'Outstanding'
        if self.order_items.all():
            total_amount = 0
            total_quantity = 0
            for item in self.order_items.all():
                total_amount += item.total_amount
                total_quantity += item.quantity
            # Calculate Extra Charge + Discount
            total_amount = total_amount + self.extra_charge - self.discount
            total_amount = (
                1 + self.payment_method.services_charge/100) * total_amount
            self.total_amount = total_amount
            self.total_quantity = total_quantity
        super(Order_ABSTRACT, self).save(*args, **kwargs)

# Inheritance from Order


class SalesOrder(Order_ABSTRACT):
    def default_group():
        return PaymemtOption.objects.get_or_create(name="Cash")[0].id

    def default_channel():
        try:
            return SalesChannel.objects.all()[0].id
        except:
            return None

    customer = models.ForeignKey(
        Customer, related_name='previous_orders', on_delete=CASCADE)
    channel = models.ForeignKey(
        SalesChannel, default=default_channel, on_delete=CASCADE)
    discount = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    extra_charge = models.DecimalField(default=0,max_digits=12, decimal_places=2)
    payment_method = models.ForeignKey(
        PaymemtOption, default=default_group, related_name='payment_options', on_delete=CASCADE)

    def __str__(self):
        output = f"{self.create_datetime}: {self.customer} ${self.total_amount}"
        return output


class StockTransferOrder(Order_ABSTRACT):
    source = models.ForeignKey(
        Warehouse, on_delete=CASCADE, related_name='%(class)s_requests_created')
    destination = models.ForeignKey(Warehouse, on_delete=CASCADE)

    def __str__(self):
        output = f"Transfer: {self.source} -> {self.destination} {self.create_datetime}"
        return output


class Item(models.Model):
    order = models.ForeignKey(
        SalesOrder, related_name='order_items', on_delete=CASCADE)
    product = models.ForeignKey(Stocklevel, on_delete=CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(
        blank=True, max_digits=12, decimal_places=2)
    total_amount = models.DecimalField(
        max_digits=12, decimal_places=2, default=0, editable=False)

    def save(self, *args, **kwargs):
        self.unit_price = self.product.price
        self.total_amount = self.quantity * self.unit_price
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        output = f"{self.product.product.name} (Qty: {self.quantity})"
        return output


class TransferItem(models.Model):
    order = models.ForeignKey(
        StockTransferOrder, related_name='order_items', on_delete=CASCADE)
    stock = models.ForeignKey(Stocklevel, on_delete=CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        output = f"{self.order}: {self.stock.product.name} {self.quantity}"
        return output

# class OrderInfo(models.Model):
#     company_name = 
#     company_address = 
#     company_tel = 
#     company_email = 
#     remark = 