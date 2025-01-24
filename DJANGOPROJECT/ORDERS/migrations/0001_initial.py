# Generated by Django 5.1.2 on 2025-01-24 01:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SHOP', '0002_items_created_items_updated'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
                'db_table': 'orders',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='OrdersLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SHOP.items')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ORDERS.orders')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'order line',
                'verbose_name_plural': 'orders line',
                'db_table': 'ordersline',
                'ordering': ['id'],
            },
        ),
    ]
