from django.db import models
from django.db.models.deletion import CASCADE


class ProductCat(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class ProductBrand(models.Model):
    name = models.CharField(max_length=64)
    other_name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    barcode = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=64)
    brand = models.ForeignKey(
        ProductBrand, related_name='product_brand',  on_delete=CASCADE)
    catagory = models.ForeignKey(
        ProductCat, related_name='product_cat', on_delete=CASCADE)

    def __str__(self):
        return f"({self.catagory}) {self.brand} {self.name}"
