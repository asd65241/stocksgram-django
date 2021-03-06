# Generated by Django 3.1.7 on 2021-04-04 14:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_auto_20210404_1458'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='order_id',
            field=models.CharField(default='ORD-8MWU18S5IMGE', editable=False, max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='projected_completed_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 11, 14, 58, 44, 442554)),
        ),
        migrations.AlterField(
            model_name='stocktransferorder',
            name='order_id',
            field=models.CharField(default='ORD-8MWU18S5IMGE', editable=False, max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='stocktransferorder',
            name='projected_completed_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 11, 14, 58, 44, 442554)),
        ),
    ]
