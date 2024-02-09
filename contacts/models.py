from django.db import models
from django.utils import timezone


class Message(models.Model):
    name = models.CharField('Имя пользователя', max_length=120)
    email = models.EmailField('Email')
    title = models.CharField('Тема сообщения', max_length=200)
    text = models.TextField('Текст сообщения')
    date = models.DateTimeField('Дата', default=timezone.now)
    read = models.BooleanField(verbose_name='Прочитано', default=False)

    def __str__(self):
        return f'Сообщение от {self.name} ({self.date})'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
