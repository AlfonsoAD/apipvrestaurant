# Generated by Django 4.2.7 on 2023-11-17 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0002_alter_table_capacity_alter_table_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='number',
            field=models.IntegerField(unique=True),
        ),
    ]
