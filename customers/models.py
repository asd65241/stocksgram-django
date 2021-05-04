from django.db import models
from django.db.models.deletion import CASCADE
import shortuuid
import datetime

# Initialize Random ID
shortuuid.set_alphabet("ABCDEFGHIJKLMNOPQRSTUVWXYZ012345678")
# To use radom id, use:
# shortuuid.uuid()[:12]

# Create your models here.
#    customer_id = models.CharField(max_length=20, blank=True, null=True, default=f"CUS-{shortuuid.uuid()[:12]}", editable=False)


class Customer(models.Model):
    TYPE = [('B2B', 'B2B'), ('B2C', 'B2C')]
    SEX = [('M', 'Male'), ('F', 'Female'), ('NA', 'NA')]
    customer_id = models.CharField(
        max_length=16, default=f"CUS-{shortuuid.uuid()[:12]}")
    type = models.CharField(max_length=3, choices=TYPE, default='B2C')
    sex = models.CharField(max_length=6, choices=SEX, default='NA')
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        output = f"{self.name} ({self.type})"
        return output
