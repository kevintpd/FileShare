from django.db import models
# from folder.models import Folder

# Create your models here.
class file(models.Model):
    #文件模型类
    #文件名
    file_name = models.CharField(verbose_name='文件名',max_length=20)
    #文件所属文件夹
    belong_to_folder = models.CharField(verbose_name='文件所属文件夹',max_length=20, default='')
    #文件大小,单位kb
    file_size = models.DecimalField(verbose_name='文件大小',max_digits=10,decimal_places=2,default='')
    #文件类型
    file_type = models.CharField(verbose_name='文件类型',max_length=10, default='')
    #文件下载次数
    download_times = models.IntegerField(verbose_name='文件下载次数',default=0)
    #文件的外键链接文件夹
    # file_blong_to_folder = models.ForeignKey('Folder', on_delete=models.CASCADE)

