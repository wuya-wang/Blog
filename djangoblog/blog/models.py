from django.db import models
from django.contrib.auth.models import AbstractUser
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
    article_category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, blank=True, null=True,
        related_name='article_category')

    def __str__(self):
        return self.title


# 文章分类
class Category(models.Model):
    category = models.CharField(max_length=32, verbose_name='分类标题')

    def __str__(self):
        return self.category


# 文章标签
class Tag(models.Model):
    tag = models.CharField(max_length=32, verbose_name='标签')
    article_tag = models.ManyToManyField(
        "Article", blank=True,
        related_name='article_tag'
    )

    def __str__(self):
        return self.tag


# 评论
class Comments(models.Model):
    text = models.TextField(verbose_name='评论内容', max_length=128, blank=True, null=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True,
                             verbose_name='评论者', related_name='user_comments')
    article = models.ForeignKey('Article', on_delete=models.CASCADE, blank=True, null=True,
                                verbose_name='评论的文章', related_name='article_comments')
    reply = models.ForeignKey('Comments', on_delete=models.SET_NULL, blank=True, null=True,
                              verbose_name='回复', related_name='comments_reply')

    def __str__(self):
        return self.text


# 收藏
class Collection(models.Model):
    state = models.BooleanField(default=False, blank=True, null=True, verbose_name='收藏状态')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True,
                             verbose_name='收藏者', related_name="collection_user")
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE, blank=True, null=True,
                                verbose_name='收藏的文章', related_name='collection_article')

    def __int__(self):
        return self.id


# 点赞
class Likes(models.Model):
    state = models.BooleanField(default=False, blank=True, null=True, verbose_name='点赞状态')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True,
                             verbose_name='点赞者', related_name='likes_user')
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE, blank=True, null=True,
                                verbose_name='点赞的文章', related_name='likes_article')

    def __int__(self):
        return self.id
