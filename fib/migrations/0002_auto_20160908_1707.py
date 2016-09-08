# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-08 11:37
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fib', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fibonacci',
            name='parameter',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]
