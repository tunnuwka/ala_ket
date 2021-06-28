from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, models.CASCADE, related_name='profile', null=True)
    first_name = models.CharField('Имя', max_length=255, blank=True, null=True)
    last_name = models.CharField('Фамилия', max_length=255, blank=True, null=True)
    phone = models.CharField('Номер телефона', max_length=30)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Stuff(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, models.CASCADE, related_name='stuff', null=True)
    first_name = models.CharField('Имя', max_length=255, blank=True, null=True)
    last_name = models.CharField('Фамилия', max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'