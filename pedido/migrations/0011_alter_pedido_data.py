# Generated by Django 4.1.1 on 2022-10-18 05:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0010_alter_pedido_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 18, 2, 43, 49, 865519)),
        ),
    ]
