from django.db import models


# Create your models here.
class Folder(models.Model):
    # 创建分享文件夹模型
    # 文件夹名称
    name = models.CharField(verbose_name="文件夹名", max_length=20)
    # 文件夹创建时间
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    # 文件夹存在时长
    exist_time = models.IntegerField(verbose_name="存在时间")
    # 文件夹所属人，文件夹的外键
    owner = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='owner', blank=True)
    # 文件夹创建者
    creator = models.CharField(verbose_name="文件夹创建者", max_length=20)
    # 文件夹分享码,有分享码则为 共享文件夹 分享码为空就是普通文件夹
    share_code = models.CharField(verbose_name="分享码", max_length=20, blank=True, null=True)
    # 文件夹权限 1代表可以上传 2代表可以删除 4代表可以下载 3代表上传和删除 5代表上传下载 6删除下载 7上传删除下载
    folder_permission = models.IntegerField()

    parent = models.ForeignKey('folder.Folder', on_delete=models.CASCADE, related_name='children', blank=True, null=True)

    def __str__(self):
        return self.name

