# Generated by Django 3.1.7 on 2021-04-03 06:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20210331_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymemtOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('services_charge', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='order_id',
            field=models.CharField(default='ORD-K07IGVP78TFL', editable=False, max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='projected_completed_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 10, 6, 6, 26, 760676)),
        ),
        migrations.AlterField(
            model_name='stocktransferorder',
            name='order_id',
            field=models.CharField(default='ORD-K07IGVP78TFL', editable=False, max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='stocktransferorder',
            name='projected_completed_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 10, 6, 6, 26, 760676)),
        ),
    ]
