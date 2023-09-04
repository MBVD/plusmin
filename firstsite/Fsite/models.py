from email.policy import default
from tabnanny import verbose

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from tinymce import models as tinymce_models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager
from datetime import datetime
import pytz
from django_countries.fields import CountryField


class MaterialSubject(models.Model):
    name = models.CharField(verbose_name = 'Предмет', unique=True, max_length=50)

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = tinymce_models.HTMLField(verbose_name='Краткое содержание', blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    author = models.CharField(max_length=50, verbose_name='Автор', default="Admin")
    tags = TaggableManager(blank=True)
    hidden_content = tinymce_models.HTMLField(verbose_name='Текст полной статьи', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news', kwargs={'news_id': self.pk})

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        ordering = ['time_update']  # сортировка


class ProblemSolution(models.Model):
    name = models.CharField(verbose_name = 'Тип Решения', unique=True, max_length=50)

    class Meta:
        verbose_name = "Решение пользователя"
        verbose_name_plural = "Решения пользователей"


class Problem(models.Model):
    subject = models.ForeignKey(MaterialSubject, on_delete=models.CASCADE, related_name="problems", null=True)
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = tinymce_models.HTMLField(verbose_name='Текст задачи', blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    author = models.CharField(max_length=50, verbose_name='Автор', default='Admin')
    source = models.CharField(max_length=50, verbose_name='Источник', default='Неизвестно')
    rate = models.IntegerField(blank=True, validators=[MinValueValidator(1), MaxValueValidator(10)], default=None, null=True)
    tags = TaggableManager(blank=True)
    correct_solution = tinymce_models.HTMLField(blank = True, verbose_name = 'Решение задачи')
    answer = models.CharField(blank=True, null = True, max_length=50, verbose_name='Ответ на задачу')
    type = models.ForeignKey(ProblemSolution, blank=True, on_delete=models.CASCADE, related_name="problems", null=True)
    show_solution = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('problems', kwargs={'problem_id': self.pk})

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['time_update']  # сортировка


class Contest(models.Model):
    name = models.CharField(verbose_name='Контест', max_length=50)
    problems = models.ManyToManyField(Problem)
    created_at = models.DateField(auto_now_add=True, verbose_name='Время создания', blank=True)
    started_at = models.DateTimeField(verbose_name = 'Дата проведения')
    completed_at = models.DateTimeField(verbose_name = 'Дата до конца')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    finished = models.BooleanField(default=False, verbose_name='Завершен')
    tags = TaggableManager(blank=True)
    registered_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = "contests", blank = True)
    judges = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = "refereeing_contests", blank = True)
    
    def is_running(self):
        return (self.started_at <= pytz.utc.localize(datetime.utcnow())) and (self.completed_at > pytz.utc.localize(datetime.utcnow()))
    
    def is_finished(self):
        statement = self.completed_at <= pytz.utc.localize(datetime.utcnow())
        self.finished = statement
        self.save()
        return statement

    def rest_of_start(self):
        if not self.is_finished() and not self.is_running():
            return self.started_at - datetime.now()

    def contest_duration(self):
        return self.completed_at - self.started_at

    class Meta:
        verbose_name = 'Контесты'
        verbose_name_plural = 'Контесты'
        ordering = ['created_at']

    def __str__(self):
        return self.name


class UserFollowing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="following", on_delete=models.CASCADE)
    following_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="followers", on_delete=models.CASCADE) # на кого подписываются
    following_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Подписки'
        verbose_name_plural = 'Подписки'


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(verbose_name="Номер телефона", null=True, blank=True)
    birth_date = models.DateTimeField(verbose_name='Дата рождения', null=True, blank=True)
    avatar = models.ImageField(blank=True, verbose_name="Фото пользователя", upload_to="images", default="logo.png")
    rate = models.IntegerField(blank=True, verbose_name="Рейтинг пользователей", default=0)
    about_me = models.TextField(blank=True, verbose_name="О себе", default="Обо мне")
    status = models.CharField(max_length=30, blank=True, verbose_name = "Статус пользователя", default="Пользователь PlusMinus")
    country = CountryField(null=True, verbose_name = 'Страна', blank=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.username


class Material(models.Model):
    content = tinymce_models.HTMLField(verbose_name='Текст', blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    author = models.CharField(max_length=50, verbose_name='Автор', default='Admin')
    source = models.CharField(max_length=50, verbose_name='Источник', default='Неизвестно')
    subject = models.ForeignKey(MaterialSubject, on_delete=models.CASCADE, related_name="materials")
    time_start = models.IntegerField(blank=True, null = True)
    time_end = models.IntegerField(blank=True, null = True)

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"


class UserSolution(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="solutions", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    contest = models.ForeignKey(Contest, on_delete = models.CASCADE, related_name = "solutions")
    problem = models.ForeignKey(Problem, on_delete = models.CASCADE, related_name = "solutions")
    text_solution = models.TextField(blank=True, verbose_name = "РешениеТекс", null = True)
    image_solution = models.ImageField(blank=True, verbose_name="РешениеФото", upload_to="user_solutions", null=True)
    mark = models.IntegerField(blank=True, validators=[MinValueValidator(0), MaxValueValidator(7)], default=None, null=True)
    
    class Meta:
        verbose_name = "Решение пользователя"
        verbose_name_plural = "Решения пользователей"


class HistoryProblem(models.Model):
    question = tinymce_models.HTMLField(verbose_name='Текст задачи')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    author = models.CharField(max_length=50, verbose_name='Автор', default='Admin')
    source = models.CharField(max_length=50, verbose_name='Источник', default='Неизвестно')
    answer = models.CharField(blank=True, null=True, max_length=50, verbose_name='Ответ на вопрос')
    show_solution = models.BooleanField(default=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос по истории'
        verbose_name_plural = 'Вопросы по истории'
        ordering = ['time_update']  # сортировка


class HistoryTestProblem(models.Model):
    question = tinymce_models.HTMLField(verbose_name='Текст задачи')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    author = models.CharField(max_length=50, verbose_name='Автор', default='Admin')
    source = models.CharField(max_length=50, verbose_name='Источник', default='Неизвестно')
    answer1 = models.CharField(max_length=50, verbose_name='Вариант 1')
    answer2 = models.CharField(max_length=50, verbose_name='Вариант 2')
    answer3 = models.CharField(max_length=50, verbose_name='Вариант 3')
    correct_answer = models.CharField(max_length=50, verbose_name='Правильный вариант')
    show_solution = models.BooleanField(default=True)

# class Comments
# class Competitions

