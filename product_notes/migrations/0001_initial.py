# Generated by Django 4.2.7 on 2023-11-16 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('details_order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('details_order', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='details_order.detailsorder')),
            ],
        ),
    ]
