# Generated by Django 5.1.3 on 2024-11-26 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0002_parkingsettings_vehicle_payment_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='license_plate',
            field=models.CharField(max_length=20),
        ),
    ]
