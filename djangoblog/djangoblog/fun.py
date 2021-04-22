# _*_ coding:utf-8 _*_
from rest_framework.authtoken.models import Token

from blog import models


def article_list(articles, user):
    article_list_data = []
    if str(user) != "AnonymousUser":
        for article in articles:
            article_info = {
                'article_id': article.id,
                'article_title': article.title,
                'article_desc': article.desc,
                'article_time': article.create_time.strftime('%Y-%m-%d %H:%I:%S'),
                'author': article.article_user.username,
                'all_likes': models.Likes.objects.filter(article=article, state=1).count(),
                'all_collections': models.Collection.objects.filter(article=article, state=1).count(),
                'all_comments': models.Comments.objects.filter(article=article).count(),
                'likes': models.Likes.objects.filter(article=article, state=1, user=user).count(),
                'collections': models.Collection.objects.filter(article=article, state=1, user=user).count(),
                'comments': models.Comments.objects.filter(article=article, user=user).count(),
            }
            article_list_data.append(article_info)
        return article_list_data
    else:
        for article in articles:
            article_info = {
                'article_id': article.id,
                'article_title': article.title,
                'article_desc': article.desc,
                'article_time': article.create_time.strftime('%Y-%m-%d %H:%I:%S'),
                'author': article.article_user.username,
                'all_likes': models.Likes.objects.filter(article=article, state=1).count(),
                'all_collections': models.Collection.objects.filter(article=article, state=1).count(),
                'all_comments': models.Comments.objects.filter(article=article).count(),
            }
            article_list_data.append(article_info)
        return article_list_data


def get_article_info(comments_list):
    comments_info = []
    for comments in comments_list:
        comments_data = {
            'user': comments.user.username,
            'text': comments.text,
            'id': comments.id,
            'father': comments.reply_id,
            'children': [],
        }
        if comments_data['father'] is not None:
            comments_data['father'] = comments.reply.user.username
        children = comments.comments_reply.all()
        if children:
            children_data = get_article_info(children)
            for i in children_data:
                comments_data['children'].append(i)
        comments_info.append(comments_data)
    return comments_info
