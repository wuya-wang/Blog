import base64
import json
import re
import time
from django.contrib.auth.hashers import check_password, make_password
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
    new_password = make_password(password)
    user = models.User(email=email, username=username, password=new_password)
    user.save()
    Token.objects.get_or_create(user=user)
    token = Token.objects.get(user=user)
    userinfo = {
        'username': user.username,
        'token': token.key,
    }
    return Response(userinfo)


@api_view(['POST'])
def login(request, ):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = models.User.objects.filter(username=username)
    print(user)
    if user:
        check_pwd = check_password(password, user[0].password)
        if check_pwd:
            user = models.User.objects.get(username=username)
            Token.objects.get_or_create(user=user)
            token = Token.objects.get(user=user)
        else:
            return Response('密码错误')
    else:
        return Response('用户名不存在')

    userinfo = {
        'token': token.key,
        'username': user.username,
    }
    return Response(userinfo)


@api_view(['POST'])
def logout(request):
    token = request.POST.get('token')
    user_token = Token.objects.get(key=token)
    user_token.delete()
    return Response('登出')


# 修改密码
@api_view(['POST'])
def change_password(request):
    token = request.POST.get('token')
    user_token = Token.objects.get(key=token)
    user_token.delete()
    return Response('登出')


# 添加文章
@api_view(['POST'])
def add_article(request):
    host = 'http://127.0.0.1:9999/'
    img = request.POST.get('img')
    if img is not None:
        img = json.loads(img)
        img_url = img['url']
        img_name = img['name']
        img_url_list = img_url.split(',')
        img_data = base64.b64decode(img_url_list[1])
        image_name = int(round(time.time() * 1000))
        img_url = 'media/img' + '/' + str(image_name) + '-' + img_name
        with open(img_url, 'wb') as f:
            f.write(img_data)
        return Response(host + img_url)
    else:
        pass
    token = request.POST.get('token')
    article_text = request.POST.get('article_text')
    article_title = request.POST.get('article_title')
    article_desc = request.POST.get('article_introduce')
    user_token = Token.objects.get(key=token)
    user = models.User.objects.get(id=user_token.user_id)
    article = models.Article(title=article_title, desc=article_desc, text=article_text, article_user=user)
    article.save()
    return Response('OK')
