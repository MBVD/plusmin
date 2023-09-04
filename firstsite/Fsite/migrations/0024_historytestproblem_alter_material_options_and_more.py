# Generated by Django 4.0.8 on 2023-03-12 13:58

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Fsite', '0023_alter_contest_tags_alter_news_tags_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryTestProblem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', tinymce.models.HTMLField(verbose_name='Текст задачи')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('author', models.CharField(default='Admin', max_length=50, verbose_name='Автор')),
                ('source', models.CharField(default='Неизвестно', max_length=50, verbose_name='Источник')),
                ('answer1', models.CharField(max_length=50, verbose_name='Вариант 1')),
                ('answer2', models.CharField(max_length=50, verbose_name='Вариант 2')),
                ('answer3', models.CharField(max_length=50, verbose_name='Вариант 3')),
                ('correct_answer', models.CharField(max_length=50, verbose_name='Правильный вариант')),
                ('show_solution', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='material',
            options={'verbose_name': 'Материал', 'verbose_name_plural': 'Материалы'},
        ),
        migrations.AlterModelOptions(
            name='materialsubject',
            options={'verbose_name': 'Предмет', 'verbose_name_plural': 'Предметы'},
        ),
        migrations.AlterModelOptions(
            name='problem',
            options={'ordering': ['time_update'], 'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.AlterModelOptions(
            name='problemsolution',
            options={'verbose_name': 'Решение пользователя', 'verbose_name_plural': 'Решения пользователей'},
        ),
        migrations.AlterField(
            model_name='problem',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Время изменения'),
        ),
    ]