# Generated by Django 3.2.5 on 2022-03-17 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='文件名')),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('download_times', models.IntegerField(default=0, verbose_name='文件下载次数')),
                ('data', models.FileField(upload_to='FileDatabase/')),
            ],
        ),
    ]
