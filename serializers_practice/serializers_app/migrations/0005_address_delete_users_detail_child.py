# Generated by Django 4.2.5 on 2023-09-19 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serializers_app', '0004_rename_user_id_user_details_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('State', models.CharField(max_length=255)),
                ('PIN_code', models.IntegerField(max_length=6)),
                ('user_details', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_details_child', to='serializers_app.user_details')),
            ],
        ),
        migrations.DeleteModel(
            name='users_detail_child',
        ),
    ]