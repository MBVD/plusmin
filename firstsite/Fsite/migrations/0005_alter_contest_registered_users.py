# Generated by Django 4.0.4 on 2022-11-10 15:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fsite', '0004_alter_userssolution_options_contest_registered_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='registered_users',
            field=models.ManyToManyField(blank=True, related_name='contests', to=settings.AUTH_USER_MODEL),
        ),
    ]
