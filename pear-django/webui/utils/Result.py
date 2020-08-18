# -*- coding:utf-8 -*-
# @File  : pear-django/Result.py
# @Author: zlx
# @Date  : 2020-07-23 9:03
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
from common_constant import SC_OK_200
from django.http import HttpResponse
import time
import json


def ok(result):
    ret = {
        'msg': "访问成功",
        'code': SC_OK_200,
        'data': {},
        'timestamp': time.strftime('yyyy-MM-dd hh:mm:ss', time.localtime()),
        'success': True
    }
    ret['data'] = result
    return HttpResponse(json.dumps(ret), content_type='application/json,charset=utf-8')


def error(msg):
    ret = {
        'msg': "访问成功",
        'code': SC_OK_200,
        'data': {},
        'timestamp': time.strftime('yyyy-MM-dd hh:mm:ss', time.localtime()),
        'success': True
    }
    ret['success'] = False
    ret['msg'] = msg
    return HttpResponse(json.dumps(ret), content_type='application/json,charset=utf-8')


def loginSuccess(user_info, token):
    ret = {
        'msg': "访问成功",
        'code': SC_OK_200,
        'userInfo': user_info,
        'token': token,
        'user_info': time.strftime('yyyy-MM-dd hh:mm:ss', time.localtime()),
        'success': True
    }
    return HttpResponse(json.dumps(ret), content_type='application/json,charset=utf-8')

