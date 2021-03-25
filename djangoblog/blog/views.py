import base64
import json
import re
import time
from django.contrib.auth.hashers import check_password, make_password
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog import models
from djangoblog import fun


# 用户名邮箱验证
@api_view(['POST'])
def uniqueness(request):
    email = request.POST.get('email')
    username = request.POST.get('username')
    if len(models.User.objects.filter(email=email)):
        return Response('邮箱已被注册')
    if len(models.User.objects.filter(username=username)):
        return Response('用户名已被使用')
    return Response('OK')


# 注册
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


# 登录
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


# 登出
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
    # 上传图片
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
    # 添加文章
    token = request.POST.get('token')
    article_text = request.POST.get('article_text')
    article_title = request.POST.get('article_title')
    article_desc = request.POST.get('article_introduce')
    article_category = request.POST.get('article_category')
    article_tag = request.POST.get('article_tag')
    # print(article_text,article_title,article_desc,article_category,article_tag)
    user_token = Token.objects.get(key=token)
    user = models.User.objects.get(id=user_token.user_id)
    # 存储外键与普通字段
    article_category_data = models.Category.objects.get(category=article_category)
    article_info = models.Article(
        title=article_title, desc=article_desc, text=article_text,
        article_user=user, article_category=article_category_data)
    article_info.save()
    # 获取多对多关系字段
    article_tag_data = models.Tag.objects.get(tag=article_tag)
    # 使用add()方法存储多对多关系
    article_info.article_tag.add(article_tag_data)
    article_info.save()
    return Response('OK')


# 文章详情
@api_view(['GET', "POST"])
def article_data(request):
    article_id = request.POST.get("id")
    token = request.POST.get('token')
    # print(token,article_id)
    user = Token.objects.get(key=token).user
    article = models.Article.objects.get(id=article_id)
    comments_list = models.Comments.objects.filter(article=article, reply=None)
    comments_info = fun.get_article_info(comments_list)
    article_info = {
        'article_title': article.title,
        'article_text': article.text,
        'article_time': article.create_time.strftime('%Y-%m-%d %H:%I:%S'),
        'author': article.article_user.username,
        'likes': models.Likes.objects.filter(article=article, state=1, user=user).count(),
        'collections': models.Collection.objects.filter(article=article, state=1, user=user).count(),
        'comments': models.Comments.objects.filter(article=article, user=user).count(),
        'comments_data': comments_info
    }
    return Response(article_info)


# 文章列表
@api_view(['POST'])
def article_list(request):
    category_data = request.POST.get('category')
    tag_data = request.POST.get('tag')
    token = request.POST.get('token')
    user = Token.objects.get(key=token).user
    if category_data is not None:
        category_id = models.Category.objects.get(category=category_data)
        articles = models.Article.objects.filter(article_category=category_id).order_by('id')
        article_list_data = fun.article_list(articles, user)
        return Response(article_list_data)
    if tag_data is not None:
        tag_id = models.Tag.objects.get(tag=tag_data)
        articles = models.Article.objects.filter(article_tag=tag_id).order_by('id')
        article_list_data = fun.article_list(articles, user)
        return Response(article_list_data)
    else:
        articles = models.Article.objects.all().order_by('id')
        article_list_data = fun.article_list(articles, user)
        return Response(article_list_data)


# 分类
@api_view(['GET', 'POST'])
def category(request):
    if request.method == 'GET':
        category_data = []
        category_all = models.Category.objects.all()
        for i in category_all:
            category_info = {
                'value': i.category,
                'label': i.category,
            }
            category_data.append(category_info)
        return Response(category_data)
    if request.method == 'POST':
        new_category = request.POST.get('new_category')
        models.Category(category=new_category).save()
    return Response('ok')


# 标签
@api_view(['GET', 'POST'])
def tag(request):
    if request.method == 'GET':
        tag_data = []
        tags = models.Tag.objects.all()
        for i in tags:
            tag_info = {
                'value': i.tag,
                'label': i.tag,
            }
            tag_data.append(tag_info)
        return Response(tag_data)
    if request.method == 'POST':
        new_tag = request.POST.get('new_tag')
        models.Tag(tag=new_tag).save()
    return Response('ok')


# 点赞
@api_view(['POST'])
def like(request):
    token = request.POST.get('token')
    article_id = request.POST.get('article_id')
    state = json.loads(request.POST.get("state"))
    user = Token.objects.get(key=token).user
    article = models.Article.objects.get(id=article_id)
    likes = models.Likes.objects.filter(article=article, user=user)
    if len(likes) != 0:
        likes.update(state=state)
    else:
        new_likes = models.Likes(user=user, article=article, state=state)
        new_likes.save()
    return Response('ok')


# 收藏
@api_view(['POST'])
def collection(request):
    token = request.POST.get('token')
    article_id = request.POST.get('article_id')
    state = json.loads(request.POST.get("state"))
    user = Token.objects.get(key=token).user
    article = models.Article.objects.get(id=article_id)
    collections = models.Collection.objects.filter(article=article, user=user)
    if len(collections) != 0:
        collections.update(state=state)
    else:
        new_collections = models.Collection(user=user, article=article, state=state)
        new_collections.save()
    return Response('ok')


# 评论
@api_view(['POST'])
def comment(request):
    token = request.POST.get('token')
    article_id = request.POST.get('article_id')
    comment_data = request.POST.get('comment')
    comment_id = request.POST.get('comment_id')
    user = Token.objects.get(key=token).user
    article = models.Article.objects.get(id=article_id)
    print(token, article_id, comment_data)
    if comment_id:
        comments = models.Comments.objects.get(id=comment_id)
        new_comment = models.Comments(article=article, user=user, text=comment_data, reply=comments)
        new_comment.save()
        return Response('ok')
    else:
        new_comment = models.Comments(article=article, user=user, text=comment_data)
        new_comment.save()
        return Response('ok')
