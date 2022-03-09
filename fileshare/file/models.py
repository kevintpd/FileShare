from django.db import models

# Create your models here.
class file(models.Model):
    filename = models.CharField('文件名',max_length=20)