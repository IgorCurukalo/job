from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    profile_name = models.CharField(max_length=250, blank=True, null=True, verbose_name='Программист/компания')
    tel = models.CharField(max_length=16, blank=True, verbose_name='Телефон')
    skills = models.ManyToManyField(
        'Skills',
        related_name='skills',
        verbose_name='Скиллы')
    id_type_user = models.ForeignKey('TypeUser',
                                     on_delete=models.CASCADE,
                                     related_name='typeuser_profile',
                                     verbose_name='Тип пользователя',
                                     null=True,
                                     blank=True)
    adr = models.CharField(max_length=250, blank=True, null=True, verbose_name='Адрес')
    biog = models.TextField(blank=True, null=True, verbose_name='Биография пользователя')
    image = models.ImageField(null=True,
                              blank=True,
                              upload_to='profile_images',
                              default="profile_images/default.jpg",
                              verbose_name='Аватар')
    github = models.CharField(max_length=100, blank=True, null=True, verbose_name='Ссылка на githab')
    twitter = models.CharField(max_length=100, blank=True, null=True, verbose_name='Ссылка на twitter')
    youtube = models.CharField(max_length=100, blank=True, null=True, verbose_name='Ссылка на youtube')
    website = models.CharField(max_length=100, blank=True, null=True, verbose_name='Ссылка на сайт')

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

class TypeUser(models.Model):
    type_user_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Тип пользователя')
    description = models.TextField(null=True, blank=True, verbose_name='Описание типа пользователя')
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_deleted = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self):
        return str(self.type_user_name)

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'типы'


class Skills(models.Model):
    skills_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Скилл')
    description = models.TextField(null=True, blank=True, verbose_name='Описание скилла')
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_deleted = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self):
        return str(self.skills_name)

    class Meta:
        verbose_name = 'Скилл'
        verbose_name_plural = 'Скиллы'


class ProfileInSkills(admin.TabularInline):

    model = Profile.skills.through