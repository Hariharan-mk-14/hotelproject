# Generated by Django 5.1.1 on 2025-02-27 09:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0002_hotel_room_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='image',
            field=models.ImageField(default=datetime.datetime(2025, 2, 27, 9, 28, 40, 784838, tzinfo=datetime.timezone.utc), upload_to='rooms/'),
            preserve_default=False,
        ),
    ]
