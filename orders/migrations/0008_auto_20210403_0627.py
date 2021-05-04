# Generated by Django 3.1.7 on 2021-04-03 06:27

import datetime
from django.db import migrations, models
import django.db.models.deletion
import orders.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20210403_0607'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorder',
            name='payment_method',
            field=models.ForeignKey(default=orders.models.SalesOrder.default_group, on_delete=django.db.models.deletion.CASCADE, related_name='payment_options', to='orders.paymemtoption'),
        ),
        migrations.AlterField(
            model_name='paymemtoption',
            name='services_charge',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='order_id',
            field=models.CharField(default='ORD-CCLMKTBROYIE', editable=False, max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='projected_completed_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 10, 6, 27, 41, 822683)),
        ),
        migrations.AlterField(
            model_name='stocktransferorder',
            name='order_id',
            field=models.CharField(default='ORD-CCLMKTBROYIE', editable=False, max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='stocktransferorder',
            name='projected_completed_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 10, 6, 27, 41, 822683)),
        ),
    ]