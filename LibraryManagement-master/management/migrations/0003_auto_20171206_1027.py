# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 02:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20160112_2031'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['name'], 'verbose_name': '书籍', 'verbose_name_plural': '书籍'},
        ),
        migrations.AlterModelOptions(
            name='img',
            options={'ordering': ['name'], 'verbose_name': '图片', 'verbose_name_plural': '图片'},
        ),
        migrations.AddField(
            model_name='book',
            name='leibie',
            field=models.IntegerField(choices=[(1, '古代'), (2, '现代')], default=1, verbose_name='图书类别'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=128, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(max_length=128, verbose_name='介绍'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=128, verbose_name='书名'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.FloatField(verbose_name='价格'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.DateField(verbose_name='出版日期'),
        ),
        migrations.AlterField(
            model_name='img',
            name='description',
            field=models.TextField(verbose_name='图片描述'),
        ),
        migrations.AlterField(
            model_name='img',
            name='img',
            field=models.ImageField(upload_to='image/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='img',
            name='name',
            field=models.CharField(max_length=128, verbose_name='图片名称'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='nickname',
            field=models.CharField(max_length=16, verbose_name='昵称'),
        ),
    ]
