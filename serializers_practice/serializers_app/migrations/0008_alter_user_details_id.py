# Generated by Django 4.2.5 on 2023-09-19 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serializers_app', '0007_alter_address_table_alter_user_details_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
