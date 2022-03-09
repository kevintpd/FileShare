from django.db import models

# Create your models here.
class ShareFolder(models.Model):
    #创建分享文件夹模型
    #文件夹名称
    foldername = models.CharField("文件夹名",max_length=20)
    #文件夹创建时间
    create_time = models.DateTimeField("创建时间",auto_now_add=True)
    #文件夹存在时长
    exist_time = models.IntegerField("存在时间")
    #文件夹所属人
    # belongtouser = models.ForeignKey()
    #文件夹分享码
    sharecode = models.CharField("分享码",max_length=20)

class CommonFolder(models.Model):
    #创建非分享文件夹
    # 文件夹名称
    foldername = models.CharField("文件夹名", max_length=20)
    # 文件夹创建时间
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    # 文件夹存在时长
    exist_time = models.IntegerField("存在时间")
    # 文件夹所属人
    # belongtouser = models.ForeignKey()