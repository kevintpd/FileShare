from django.db import models

# Create your models here.
class Folder(models.Model):
    #创建分享文件夹模型
    #文件夹名称
    foldername = models.CharField("文件夹名",max_length=20)
    #文件夹创建时间
    create_time = models.DateTimeField("创建时间",auto_now_add=True)
    #文件夹存在时长
    exist_time = models.IntegerField("存在时间")
    #文件夹所属人
    # belongtouser = models.ForeignKey()
    #文件夹创建者
    foldercreater = models.CharField("文件夹创建者",max_length=20)
    #文件夹分享码,有分享码则为 共享文件夹 分享码为空就是普通文件夹
    sharecode = models.CharField("分享码",max_length=20)
    #文件夹权限 1代表可以上传 2代表可以删除 4代表可以下载 3代表上传和删除 5代表上传下载 6删除下载 7上传删除下载
    folderpermission = models.IntegerField()

