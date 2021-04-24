#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
# Time : 2021/4/24 20:30
# Author : Wuya
import os
from celery import Celery


# 为celery程序设置默认的Django设置模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoblog.settings')

# 实例化celery应用
# 第一个是应用名称，必须指定
app = Celery('djangoblog')
app.conf.timezone = "Asia/Shanghai"

# 指定celery的配置来源
app.config_from_object('django.conf:settings')

# 自动从所有已注册的Django应用程序配置中加载任务模块
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')