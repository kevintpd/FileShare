from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    nickname = models.CharField('昵称', max_length=100, blank=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_mod_time = models.DateTimeField('修改时间', auto_now_add=True)
    source = models.CharField("创建来源", max_length=100, blank=True)

    def __str__(self):
        return self.username

class Token(models.Model):
    user_name = models.CharField('用户名', max_length=100, blank=False)
    token = models.CharField('Token' ,max_length=100, blank=False)
    create_time = models.DateTimeField('创建时间', default=datetime.now)
