# Generated by Django 3.1.7 on 2021-04-03 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_auto_20210403_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='CUS-FM2RZYZTTJLM', max_length=16),
        ),
    ]
