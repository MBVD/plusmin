# Generated by Django 4.0.4 on 2022-11-11 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Fsite', '0009_news_hidden_content_alter_news_content'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UsersSolution',
            new_name='UserSolution',
        ),
    ]
