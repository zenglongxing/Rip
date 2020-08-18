# -*- coding:utf-8 -*-
# @File  : pear/urls.py
# @Author: zlx
# @Date  : 2020-06-26 16:59
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

from django.urls import path
from .views import *

urlpatterns = [
    path(r'star/', get_hot_actor),
    path(r'movie/', get_movie),
    path(r'desc/', get_describe),
    path(r'photo/', get_photo),
    path(r'source/', get_source)
]
