from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Links(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    long_link = models.URLField('Длинная ссылка')
    slug = models.SlugField('Короткая ссылка (URL)', unique=True, help_text='*Уникальное поле, только латинские буквы и цифры')
    name_link = models.CharField('Краткое описание', max_length=200, null=True, default='Ссылка')

    def get_absolute_url(self):
        return reverse('short')

    def __str__(self):
        return f'Ссылка {self.user.username} - {self.slug}'

    class Meta:
        verbose_name = 'Ссылки'
        verbose_name_plural = 'Ссылка'
