# Generated by Django 5.0.1 on 2024-01-21 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='account_type',
            field=models.CharField(choices=[('full', 'Полный пакет'), ('free', 'Бесплатный пакет')], default='free', max_length=30),
        ),
    ]