# Generated by Django 4.0.4 on 2022-11-12 03:21

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Fsite', '0012_alter_contest_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True, verbose_name='Страна'),
        ),
    ]
