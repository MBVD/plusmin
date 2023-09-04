# Generated by Django 4.0.4 on 2022-11-10 07:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fsite', '0003_userssolution_mark_userssolution_text_solution_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userssolution',
            options={'verbose_name': 'Решение пользователя', 'verbose_name_plural': 'Решения пользователей'},
        ),
        migrations.AddField(
            model_name='contest',
            name='registered_users',
            field=models.ManyToManyField(related_name='contests', to=settings.AUTH_USER_MODEL),
        ),
    ]