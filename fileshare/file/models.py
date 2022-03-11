from django.db import models


# Create your models here.
class File(models.Model):
    # 文件模型类
    # 文件名
    name = models.CharField(verbose_name='文件名', max_length=20)
    # 文件大小,单位kb
    size = models.DecimalField(verbose_name='文件大小', max_digits=10, decimal_places=2, default='')
    # 文件类型
    file_type = models.CharField(verbose_name='文件类型', max_length=10, default='')
    # 文件下载次数
    download_times = models.IntegerField(verbose_name='文件下载次数', default=0)
    # 文件的外键链接文件夹
    related_folder = models.ForeignKey('folder.Folder', on_delete=models.CASCADE)

    data = models.FileField(upload_to='FileDatabase/')

    def __str__(self):
        return self.name
