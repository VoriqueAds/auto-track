# Generated by Django 5.1 on 2024-09-14 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_shift',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]