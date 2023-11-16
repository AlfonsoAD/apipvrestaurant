# Generated by Django 4.2.7 on 2023-11-16 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        ('products', '0002_alter_product_category'),
        ('details_order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailsorder',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.order'),
        ),
        migrations.AddField(
            model_name='detailsorder',
            name='product',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product'),
        ),
    ]