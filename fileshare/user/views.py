from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Token
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.core import signing
import time
import hashlib
from datetime import datetime
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


HEADER = {
    'type':'JWT',
    'alg':'HS256'
}

def Encrypt(value):
    data = signing.dumps(value)
    data = signing.b64_encode(data.encode()).decode()
    return data

def Decrypt(value):
    data = signing.b64_decode(value.encode()).decode()
    data = signing.loads(data)
    return data

def CreatToken(headers,payloads):
    header = Encrypt(headers)
    payload = Encrypt(payloads)
    md5 = hashlib.md5()
    md5.update(("%s.%s" % (header, payload)).encode())
    signature = md5.hexdigest()
    token = "%s.%s.%s" % (header, payload, signature)
    return token

def login_view(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        pass_word = request.POST['password']
        # 用authenticate来验证用户账号密码是否正确
        user = authenticate(request=request, username=user_name, password=pass_word)
        if user is not None:
            headers = HEADER
            data = {'user': user.username}
            payloads = {'iss': user.username,'iat': time.time()}
            token = CreatToken(headers, payloads)
            #判断该用户是否已经创建token在数据表中
            from_db = Token.objects.filter(user_name=user_name)
            if from_db:
                from_db.delete()
            #创建新的user-token到数据库
            Token.objects.create(user_name=user_name,token=token)
            #返回网页
            response = HttpResponse('login success!')
            response.set_cookie('Token',token )
            return response
        else:
            info = '账号或者密码错误！'
            return render(request, 'login.html', {'info': info})
    elif request.method == 'GET':
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/index')

def register_view(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        pass_word_1 = request.POST['password_1']
        pass_word_2 = request.POST['password_2']
        user_email = request.POST.get('useremail')
        print(user_email)
        if user_name == '':
            info = '用户名为空！'
            return render(request, 'register.html', {'info': info})
        if pass_word_1 != pass_word_2:
            info = '两次密码不一样'
            return render(request, 'register.html', {'info': info})
        user = User.objects.filter(username=user_name)
        if user:
            info = '该用户已存在'
            return render(request, 'register.html', {'info': info})
        else:
            User.objects.create_user(username=user_name, password=pass_word_1, email=user_email)
            return HttpResponseRedirect('/login')
    return render(request, 'register.html')
