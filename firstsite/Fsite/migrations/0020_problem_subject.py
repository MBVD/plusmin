# Generated by Django 4.0.4 on 2022-11-30 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Fsite', '0019_problem_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='problems', to='Fsite.materialsubject'),
        ),
    ]
