# Generated by Django 5.1 on 2024-09-18 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_brand_alter_car_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='plate',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
