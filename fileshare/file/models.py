from django.db import models

# Create your models here.
class file(models.Model):
    #文件模型类
    #文件名
    filename = models.CharField('文件名',max_length=20)
    #文件所属文件夹
    belongtofolder = models.CharField('文件所属文件夹',max_length=20, default='')
    #文件大小,单位kb
    filesize = models.DecimalField('文件大小',max_digits=10,decimal_places=2,default='')
    #文件类型
    filetype = models.CharField('文件类型',max_length=10, default='')
    #文件下载次数
    downloadtimes = models.IntegerField('文件下载次数',default='')