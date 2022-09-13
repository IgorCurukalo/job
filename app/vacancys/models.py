from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User

#вакансии
class Vakancys(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="", verbose_name='Компания')
    vakancy_name = models.CharField(max_length=100, verbose_name='Название вакансии')
    salary = models.CharField(max_length=10, null=False, blank=True, default="з/п не указана", verbose_name='Заработная плата')
    description = models.TextField(max_length=3000, verbose_name='Описание вакансии')
    experience = models.CharField(max_length=3, verbose_name='Опыт работы')
    busyness = models.ForeignKey(
        'Busyness',
        on_delete=models.CASCADE,
        related_name='busyness_vakancys',
        verbose_name='Занятость',
        null=True,
        blank=True
    )
    count = models.CharField(max_length=5, verbose_name='Количество просмотров')
    tasks = models.ManyToManyField(
        'Tasks',
        related_name='vakancys',
        verbose_name='Задачи'
    )
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_deleted = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self):
        return f'{self.vakancy_name}'

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


#Занятость
class Busyness(models.Model):
    busyness_name = models.CharField(max_length=300, verbose_name='Название занятости')
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_daleted = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self):
        return self.busyness_name

    class Meta:
        verbose_name = 'Занятость'
        verbose_name_plural = 'Занятости'

#Задачи, которые требует решить
class Tasks(models.Model):
    tasks_name = models.TextField(max_length=3000, verbose_name='Описание задачи')
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_daleted = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self):
        return self.tasks_name

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class VakancysInTasks(admin.TabularInline):

    model = Vakancys.tasks.through