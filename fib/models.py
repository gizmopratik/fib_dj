from __future__ import unicode_literals
from django.core import validators
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.

class Fibonacci(models.Model):
    parameter = models.IntegerField(primary_key = True, validators=[
            MaxValueValidator(92),
            MinValueValidator(1)
        ])
    result = models.BigIntegerField()
