# Generated by Django 4.1 on 2022-10-02 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_profile_name'),
        ('vacancys', '0019_remove_vakancys_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='vakancys',
            name='meta',
            field=models.ManyToManyField(to='users.skills', verbose_name='Скиллы'),
        ),
    ]
