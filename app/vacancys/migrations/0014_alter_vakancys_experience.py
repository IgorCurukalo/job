# Generated by Django 4.1 on 2022-10-02 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancys', '0013_remove_vakancys_user_vakancys_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vakancys',
            name='experience',
            field=models.CharField(max_length=100, verbose_name='Опыт работы'),
        ),
    ]