import re
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog import models


@api_view(['POST'])
def uniqueness(request):
    email = request.POST.get('email')
    username = request.POST.get('username')
    if len(models.User.objects.filter(email=email)):
        return Response('邮箱已被注册')
    if len(models.User.objects.filter(username=username)):
        return Response('用户名已被使用')
    return Response('OK')


@api_view(['POST'])
def register(request):
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    reward = request.POST['reward']
    # 验证信息
    re_email = re.search(r'^([a-zA-Z]|[0-9])(\w|)+@[a-zA-Z0-9]+\.([a-zA-Z]{2,4})$', email)
    if re_email:
        pass
    else:
        return Response('error_email')
    re_username = re.search(r'^[a-zA-Z0-9_-]{4,16}$', username)
    if re_username:
        pass
    else:
        return Response('error_username')
    re_password = re.search(r'^.*(?=.{8,})(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&*?.]).*$', password)
    re_reward = re.search(r'^.*(?=.{8,})(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&*?.]).*$', reward)
    if re_password and re_reward:
        pass
    else:
        return Response('error_password')
    if password != reward:
        return Response('密码不一致')
    user = models.User(email=email, username=username, password=password)
    user.save()
    Token.objects.get_or_create(user=user)
    token = Token.objects.get(user=user)
    userinfo = {
        'email': user.email,
        'password': user.password,
        'token': token.key,
    }
    return Response(userinfo)


@api_view(['POST'])
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username, password)
    user = models.User.objects.filter(username=username)
    if user:
        check_pwd = check_password(password, user[0].password)
        if check_pwd:
            user = models.User.objects.get(username=username)
            Token.objects.get_or_create(user=user)
            token = Token.objects.get(user=user)
        else:
            return Response('密码错误')
    else:
        return Response('邮箱未注册')

    userinfo = {
        'token': token.key,
        'username': user.username,
    }
    return Response(userinfo)




