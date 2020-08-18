# -*- coding:utf-8 -*-
# @File  : pear-django/render_response.py
# @Author: zlx
# @Date  : 2020-07-18 19:57
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
from rest_framework.renderers import JSONRenderer
from common_constant import SC_OK_200
import time


class customrenderer(JSONRenderer):
    # 重构render方法
    def render(self, data, accepted_media_type=None, renderer_context=None):
        msg = "访问成功"
        code = SC_OK_200
        success = True
        if data and isinstance(data, dict) and 'exception' in data:
            code = data['code']
            msg = data['message']
            success = False
        ret = {
            'message': msg,
            'code': code,
            'data': data,
            'timestamp': time.strftime(r'%Y-%m-%d %H:%M:%S', time.localtime()),
            'success': success
        }

        return super().render(ret, accepted_media_type, renderer_context)
