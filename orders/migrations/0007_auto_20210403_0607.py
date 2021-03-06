# Generated by Django 3.1.7 on 2021-04-03 06:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20210403_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorder',
            name='order_id',
            field=models.CharField(default='ORD-O7TPJB7TUO1Y', editable=False, max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='projected_completed_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 10, 6, 7, 12, 857606)),
        ),
        migrations.AlterField(
            model_name='stocktransferorder',
            name='order_id',
            field=models.CharField(default='ORD-O7TPJB7TUO1Y', editable=False, max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='stocktransferorder',
            name='projected_completed_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 10, 6, 7, 12, 857606)),
        ),
    ]
