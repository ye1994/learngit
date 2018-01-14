# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 01:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20171206_1027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '书籍', 'verbose_name_plural': '书籍'},
        ),
        migrations.AlterModelOptions(
            name='img',
            options={'verbose_name': '图片', 'verbose_name_plural': '图片'},
        ),
        migrations.RemoveField(
            model_name='book',
            name='leibie',
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(max_length=128, verbose_name='类别'),
        ),
    ]