# Generated by Django 4.2.7 on 2023-11-16 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
        ('details_menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailsmenu',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='menus.menu'),
        ),
    ]