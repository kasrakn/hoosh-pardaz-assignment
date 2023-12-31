# Generated by Django 4.2.8 on 2023-12-31 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0002_alter_shipment_tracking_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_city', models.CharField(max_length=255)),
                ('temprature', models.FloatField()),
                ('description', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameModel(
            old_name='Shipment',
            new_name='ShipmentModel',
        ),
    ]
