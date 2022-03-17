from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('folders/', views.FolderList.as_view()),
    path('folders/<int:pk>/', views.FolderDetail.as_view()),
    path('files/', views.FileList.as_view()),
    path('files/<int:pk>/', views.FileDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
