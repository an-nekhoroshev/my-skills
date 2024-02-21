# Generated by Django 5.0.2 on 2024-02-20 15:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='users_images/default.png', upload_to='users_images')),
                ('gender', models.CharField(blank=True, choices=[('male', 'Мужской'), ('female', 'Женский')], max_length=10, verbose_name='Пол')),
                ('notifications', models.BooleanField(default=True, verbose_name='Подписка на новости')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профайл',
                'verbose_name_plural': 'Профайлы',
            },
        ),
    ]
