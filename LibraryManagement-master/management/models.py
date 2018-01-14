from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=16,verbose_name='昵称')
    permission = models.IntegerField(default=1)
    def __str__(self):
        return self.user.username
class Book(models.Model):
    name = models.CharField(max_length=128,verbose_name='书名')
    price = models.FloatField(verbose_name='价格')
    author = models.CharField(max_length=128,verbose_name='作者')
    publish_date = models.DateField(verbose_name='出版日期')
    category = models.CharField(max_length=128,verbose_name='类别')

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
class Img(models.Model):
    name = models.CharField(max_length=128,verbose_name='图片名称')
    description = models.TextField(verbose_name='图片描述')
    img = models.ImageField(upload_to='image/%Y/%m/%d/')
    book = models.ForeignKey(Book)

    class Meta:
        verbose_name = '图片'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
