# Generated by Django 5.1.1 on 2025-02-27 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0003_room_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='hotel',
        ),
    ]
