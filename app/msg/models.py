from django.db import models
from app.users.models import Profile


class Msg(models.Model):
    sender = models.ForeignKey(Profile,
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True,
                               verbose_name='Отправитель')
    recipient = models.ForeignKey(Profile,
                                  on_delete=models.CASCADE,
                                  null=True,
                                  blank=True,
                                  related_name="message",
                                  verbose_name="Получатель")
    name_msg = models.CharField(max_length=250, null=False, blank=True, verbose_name='Тема')
    body = models.TextField(null=False, verbose_name='сообщение')
    is_read = models.BooleanField(default=False, null=True, verbose_name='статус сообщения')
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='дата/время создания')

    def __str__(self):
        return f'{self.name_msg}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['is_read', '-date_add']
