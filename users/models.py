from django.db import models
from django.contrib.auth.models import User
from PIL import Image

CHOISES = (('male', 'Мужской'), ('female', 'Женский'))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='users_images/default.png', upload_to='users_images')
    gender = models.CharField(max_length=10, choices=CHOISES, verbose_name='Пол', blank=True)
    notifications = models.BooleanField(verbose_name='Подписка на новости', default=True)

    def __str__(self):
        return f'Профайл пользователя {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)

        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)

    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'
