# -*- coding:utf-8 -*-
# @File  : pear-django/urls.py
# @Author: zlx
# @Date  : 2020-07-22 9:51
# @Desc  : 机器学习
# 代码神兽
#  ┏┓　　　┏┓
# ┏┛┻━━━┛┻┓
# ┃　　　　　　　┃ 　
# ┃　　　━　　　┃
# 　┳┛　┗┳　┃
# 　　　　　　　┃
# 　　　┻　　　┃
# 　　　　　　　┃
# ┗━┓　　　┏━┛
# 　　┃　　　┃神兽保佑
# 　　┃　　　┃代码无BUG！
# 　　┃　　　┗━━━┓
# 　　┃　　　　　　　┣┓
# 　　┃　　　　　　　┏┛
# 　　┗┓┓┏━┳┓┏┛
# 　　　┃┫┫　┃┫┫
# 　　　┗┻┛　┗┻┛
from django.urls import path, re_path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path(r'register', register),
    path(r'login', LoginAPIView.as_view())
]
