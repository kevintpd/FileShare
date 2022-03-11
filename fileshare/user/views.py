from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import login
from django.contrib.auth import authenticate

# Create your views here.

"""
# 1、用户登录
# 1.1获取客户端传过来的数据
# 1.2在数据库查询是否有正确
# 1.2.1正确，跳转至主页面
# 1.2.3错误，信息错误，返回登录界面
# 2、用户注册
# 2.1点击注册跳转至注册界面
# 2.2填写信息
# 2.3点击注册后，后端数据库验证
# 2.4如果用户已经存在，则注册成功，跳转至登录界面
# 2.5如果验证失败，返回注册界面，显示用户已存在
"""


class CustomBackend(ModelBackend):
    # 方法重写
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except Exception as e:
            return None


def login_view(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        pass_word = request.POST['password']
        # 用authenticate来验证用户账号密码是否正确
        user = authenticate(request=request, username=user_name, password=pass_word)
        if user is not None:
            # 保持登录状态
            login(request, user)
            return HttpResponseRedirect('/index')
        else:
            return render(request, 'login.html', {'msg': '账号或者密码错误！'})
    elif request.method == 'GET':
        return render(request, 'login.html')


def register_view(request):
    return render(request, 'register.html')
