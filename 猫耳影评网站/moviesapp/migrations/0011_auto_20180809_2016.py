# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-09 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp', '0010_auto_20180809_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviesinfo',
            name='critics_num',
        ),
        migrations.AlterField(
            model_name='moviesinfo',
            name='score',
            field=models.CharField(max_length=4, verbose_name='豆瓣评分'),
        ),
    ]
