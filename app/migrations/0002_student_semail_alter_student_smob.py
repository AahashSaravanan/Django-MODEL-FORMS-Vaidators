# Generated by Django 5.0.6 on 2024-08-13 05:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='semail',
            field=models.EmailField(default='student@gmail.com', max_length=254, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='student',
            name='smob',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('[6-9]/d{9}')]),
        ),
    ]
