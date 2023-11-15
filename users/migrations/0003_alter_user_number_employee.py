# Generated by Django 4.2.7 on 2023-11-15 06:20

from django.db import migrations, models
import shortuuid.main


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_number_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='number_employee',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=22),
        ),
    ]
