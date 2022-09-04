from django.contrib import admin
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True,
                              blank=True,
                              upload_to='profile_project',
                              default="profile_project/default.jpg",
                              verbose_name='Фото проекта')
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=500, null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_deleted = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

