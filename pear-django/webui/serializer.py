# -*- coding:utf-8 -*-
# @File  : pear/serializer.py.py
# @Author: zlx
# @Date  : 2020-07-06 15:45
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
from rest_framework import serializers
from crawl.models import *


class starSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = '__all__'


class movieSerializer(serializers.ModelSerializer):
    star = starSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


class photoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class sourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'
