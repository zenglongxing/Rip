# -*- coding:utf-8 -*-
# @File  : pear/urls.py
# @Author: zlx
# @Date  : 2020-06-26 17:00
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

from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from crawl.views import get_path, get_login
from .views import *

router = DefaultRouter()
router.register('star', StarViewSet)
router.register('movie', MovieViewSet)
router.register('photo', PhotoViewSet)
router.register('source', SourceViewSet)

urlpatterns = [
    re_path('^', include(router.urls)),
    path(r'videoPath/', get_path),
    path(r'crawlLogin/', get_login),
]
