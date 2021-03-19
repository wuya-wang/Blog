from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.


# 用户
class User(AbstractUser):
    nickname = models.CharField(max_length=16, verbose_name='昵称', null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', verbose_name='头像', default='', null=True, blank=True)

    def __str__(self):
        return self.username


# 文章
class Article(models.Model):
    title = models.CharField(verbose_name='标题', max_length=128, blank=True, null=True)
    desc = models.CharField(verbose_name='简介', max_length=255, blank=True, null=True)
    text = models.TextField(verbose_name='内容')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    article_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='文章作者')

    def __str__(self):
        return self.title


# 文章分类
class Category(models.Model):
    category = models.CharField(max_length=32, verbose_name='分类标题')
    relation = models.ForeignKey(
        'Article', on_delete=models.SET_NULL, blank=True, null=True,
        related_name='article_category'
    )

    def __str__(self):
        return self.category


# 文章标签
class Tag(models.Model):
    tag = models.CharField(max_length=32, verbose_name='标签')
    relation = models.ManyToManyField(
        "Article", blank=True, null=True,
        related_name='article_tag'
    )

    def __str__(self):
        return self.tag
