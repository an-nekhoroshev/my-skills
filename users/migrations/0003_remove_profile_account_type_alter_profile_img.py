# Generated by Django 5.0.1 on 2024-02-03 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_account_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='account_type',
        ),
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='default.png', upload_to='users_images'),
        ),
    ]
