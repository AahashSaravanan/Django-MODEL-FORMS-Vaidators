from django.db import models
from django.core import validators

# Create your models here.

class Student(models.Model):
    sname=models.CharField(max_length=10)
    sage=models.IntegerField()
    sid=models.IntegerField(primary_key=True)
    semail = models.EmailField(default='student@gmail.com',validators=[validators.EmailValidator()])
    smob=models.CharField(max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    sdept=models.CharField(max_length=20)