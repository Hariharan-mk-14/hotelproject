# Generated by Django 5.1.1 on 2025-03-13 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0008_alter_booking_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
