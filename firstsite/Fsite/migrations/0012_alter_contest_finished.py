# Generated by Django 4.0.4 on 2022-11-12 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fsite', '0011_alter_usersolution_image_solution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='finished',
            field=models.BooleanField(default=False, verbose_name='Завершен'),
        ),
    ]
