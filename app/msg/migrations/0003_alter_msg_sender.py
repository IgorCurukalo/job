# Generated by Django 4.1 on 2022-10-28 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_profile_name'),
        ('msg', '0002_alter_msg_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='msg', to='users.profile', verbose_name='Отправитель'),
        ),
    ]