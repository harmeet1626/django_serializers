# Generated by Django 4.2.5 on 2023-09-19 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serializers_app', '0006_alter_address_pin_code'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='address',
            table='address',
        ),
        migrations.AlterModelTable(
            name='user_details',
            table='user_details',
        ),
    ]
