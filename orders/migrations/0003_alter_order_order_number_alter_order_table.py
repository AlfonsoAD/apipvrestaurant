# Generated by Django 4.2.7 on 2023-11-16 20:33

from django.db import migrations, models
import django.db.models.deletion
import handlers.order_handler


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0002_alter_table_capacity_alter_table_number'),
        ('orders', '0002_alter_order_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(default=handlers.order_handler.order_number_create, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='table',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.table'),
        ),
    ]
