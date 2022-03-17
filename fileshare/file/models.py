from django.db import models


class File(models.Model):
    # 文件模型类
    # 文件名
    name = models.CharField(verbose_name='文件名', max_length=20)

    owner = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='owned_files', blank=True)

    uploaded_date = models.DateTimeField(auto_now_add=True)

    # 文件下载次数
    download_times = models.IntegerField(verbose_name='文件下载次数', default=0)
    # 文件的外键链接文件夹
    related_folder = models.ForeignKey('folder.Folder', on_delete=models.CASCADE, related_name='files')

    data = models.FileField(upload_to='FileDatabase/')

    def __str__(self):
        return self.name
