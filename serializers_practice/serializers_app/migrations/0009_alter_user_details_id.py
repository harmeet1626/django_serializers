# Generated by Django 4.2.5 on 2023-09-20 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serializers_app', '0008_alter_user_details_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
