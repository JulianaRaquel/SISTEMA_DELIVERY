# Generated by Django 4.1.5 on 2023-01-24 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0013_pedido_cupom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='usuario',
            field=models.CharField(max_length=30),
        ),
    ]
