from rest_framework import serializers
from django.apps import apps
import os

Folder = apps.get_model('folder', 'Folder')
File = apps.get_model('file', 'File')
User = apps.get_model('user', 'User')


class FolderSerializer(serializers.ModelSerializer):
    owner_name = serializers.ReadOnlyField(source='owner.username')
    files = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    children = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Folder

        fields = (
            'id', 'name', 'create_time', 'owner', 'owner_name', 'share_code', 'folder_permission', 'parent', 'files',
            'children')


class FileSerializer(serializers.ModelSerializer):
    size = serializers.ReadOnlyField(source='data.size')
    extension = serializers.SerializerMethodField()
    owner_name = serializers.ReadOnlyField(source='owner.username')

    @staticmethod
    def get_extension(obj):
        split = os.path.splitext(obj.data.name)
        return split[-1]

    class Meta:
        model = File
        fields = (
            'id', 'name', 'owner', 'owner_name', 'extension', 'size', 'uploaded_date', 'download_times',
            'related_folder', 'data')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
