# Generated by Django 4.0.2 on 2022-03-09 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foldername', models.CharField(max_length=20, verbose_name='文件夹名')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('exist_time', models.IntegerField(max_length=8, verbose_name='存在时间')),
            ],
        ),
    ]
