from rest_framework import generics
from django.apps import apps
from .serializers import FolderSerializer, FileSerializer, UserSerializer
# from ..user.models import Token

Folder = apps.get_model('folder', 'Folder')
File = apps.get_model('file', 'File')
User = apps.get_model('user', 'User')



class FolderList(generics.ListCreateAPIView):
    queryset = Folder.objects.all().order_by('create_time')
    serializer_class = FolderSerializer


class FolderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


class FileList(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class FileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class TokenList(generics.ListCreateAPIView):
#     queryset = Token.object.all()
#     serializer_class = TokenSerializer
#
# class TokenDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Token.object.all()
#     serializer_class = TokenSerializer