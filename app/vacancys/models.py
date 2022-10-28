from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from app.users.models import Profile, Skills


#вакансии
class Vakancys(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default="", verbose_name='Компания')
    vakancy_name = models.CharField(max_length=100, null=False, blank=True, verbose_name='Название вакансии')
    salary = models.CharField(max_length=100, null=False, blank=True, default="з/п не указана", verbose_name='Заработная плата')
    description = models.TextField(max_length=3000, verbose_name='Описание вакансии')
    tasks = models.TextField(max_length=3000, default=" ", verbose_name='Описание задачи')
    experience = models.CharField(max_length=100, verbose_name='Опыт работы')
    busyness = models.ForeignKey(
        'Busyness',
        on_delete=models.CASCADE,
        related_name='busyness_vakancys',
        verbose_name='Занятость',
        null=True,
        blank=True
    )
    skills = models.ManyToManyField(Skills, verbose_name='Скиллы')
    count = models.CharField(max_length=10, default="0", verbose_name='Количество просмотров')
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
    is_deleted = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self):
        return self.busyness_name

    class Meta:
        verbose_name = 'Занятость'
        verbose_name_plural = 'Занятости'


class VakancysInSkills(admin.TabularInline):
    model = Vakancys.skills.through