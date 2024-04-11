# Generated by Django 5.0.4 on 2024-04-10 21:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pedidos', '0002_alter_pedidos_estado'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pedidos.pedidos')),
                ('productos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='productos.productos')),
            ],
        ),
    ]
