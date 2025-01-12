# Generated by Django 5.1 on 2024-09-16 22:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_car_car_shift'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='car_brand', to='cars.brand'),
        ),
    ]
