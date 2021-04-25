#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
# Time : 2021/4/24 20:37
# Author : Wuya
import random
import time
from celery.signals import task_success
from celery import shared_task
from django.core.mail import send_mail
from djangoblog.settings import EMAIL_HOST_USER
from django.core.cache import cache


@shared_task
def email(e_mail):
    msg = str(random.randint(100000, 999999))
    send_mail(
        subject='验证码',
        message=msg,
        from_email=EMAIL_HOST_USER,
        recipient_list=[e_mail]
    )
    cache.set(e_mail, msg, 30 * 60)
    print(cache.get(e_mail))
