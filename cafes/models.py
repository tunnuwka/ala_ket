from typing import Text
from django.db import models
from django.db.models.fields import CharField, TextField


class FranshizaCafe(models.Model):
    cafe = models.CharField('Название франшизы кафе, ресторанов', max_length=100)

    class Meta:
        verbose_name = 'Франшиза'
        verbose_name_plural = 'Франшизы'

    def __str__(self):
        return self.cafe


class Cafe(models.Model):
    cafe_franshiza = models.ForeignKey('cafes.FranshizaCafe', models.CASCADE, related_name='cafe_c', null=True)
    cafe = models.CharField('Кафе', max_length=100)
    address = models.CharField('Адрес', max_length=255)
    phone = models.CharField('Телефон', max_length=30)

    class Meta:
        verbose_name = 'Кафе'
        verbose_name_plural = 'Кафешки'

    def __str__(self):
        return self.cafe


class Announcement(models.Model):
    cafe = models.ForeignKey('cafes.Cafe', models.CASCADE, related_name='announcement_cafe', null=True)
    news = models.CharField('Новости', max_length=255)
    text = models.TextField('Текст')
    image = models.FileField('Изображение', upload_to='announcement_image/', blank=True)
    date = models.DateTimeField('Дата', auto_now_add=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.news


class Comment(models.Model):
    announcement = models.ForeignKey('cafes.Announcement', models.CASCADE, related_name='annoucement_comments', null=True)
    user = models.ForeignKey('users.Profile', models.CASCADE, related_name='users_comments', null=True)
    text = models.TextField('Комментарии')
    date = models.DateTimeField('Дата', auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text
 
