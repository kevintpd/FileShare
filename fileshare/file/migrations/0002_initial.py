# Generated by Django 3.2.5 on 2022-03-17 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('file', '0001_initial'),
        ('folder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='owner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_files', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='file',
            name='related_folder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='folder.folder'),
        ),
    ]
