from django.db import models
from django.db.models.deletion import CASCADE
from products.models import *
from django.core.validators import MinValueValidator

class Warehouse(models.Model):
    TYPE = [('W', 'Warehouse'), ('S', 'Store')]
    name = models.CharField(max_length=64, unique=True)
    type = models.CharField(max_length=1, choices=TYPE)

    def __str__(self):
        output = f"{self.name} ({self.type})"
        return output

class Stocklevel(models.Model):
    product = models.ForeignKey(Product,related_name='product_stock', on_delete=CASCADE)
    storage = models.ForeignKey(Warehouse,related_name='instock_products', on_delete=models.PROTECT)
    expiry_date = models.DateField(blank=True, null=True)
    stock_unit = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    price = models.DecimalField(max_digits=12, decimal_places=2)
    cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        if self.remark:
            return f"{self.product.name} (Total Stock:{self.stock_unit}|Remark:{self.remark})"
        else:
            return f"{self.product.name} (Total Stock:{self.stock_unit})"

