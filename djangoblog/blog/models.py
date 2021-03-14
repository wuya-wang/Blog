from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


# 用户
class User(AbstractUser):
    nickname = models.CharField(max_length=16, verbose_name='昵称', null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', verbose_name='头像', default='', null=True, blank=True)

    def __str__(self):
        return self.username
