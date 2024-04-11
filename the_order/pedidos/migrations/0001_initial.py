# Generated by Django 5.0.4 on 2024-04-10 20:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=100)),
                ('para_llevar', models.BooleanField(default=False)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('estado', models.CharField(default='pendiente', max_length=20, null=True)),
                ('cantidad', models.CharField(default=1, max_length=20)),
                ('productos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='productos.productos')),
            ],
        ),
    ]
