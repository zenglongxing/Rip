# -*- coding:utf-8 -*-
# @File  : pear-django/authentications.py
# @Author: zlx
# @Date  : 2020-07-27 21:09
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
import jwt
from rest_framework.exceptions import AuthenticationFailed
from redis.exceptions import ConnectionError
from rest_framework_jwt.authentication import jwt_decode_handler
from pear.settings import CACHE_TIMEOUT, CACHE_PREFIX
from django.core.cache import cache
from rest_framework_jwt.authentication import get_authorization_header
from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication


class JSONWebTokenAuthentication(BaseJSONWebTokenAuthentication):
    def authenticate(self, request):
        jwt_value = get_authorization_header(request)

        if not jwt_value:
            raise AuthenticationFailed('Authorization 字段是必须的')
        try:
            payload = jwt_decode_handler(jwt_value)
            token_key = CACHE_PREFIX + jwt_value.decode()
            timeout = cache.ttl(token_key)
            if timeout == 0:
                raise AuthenticationFailed('Token失效，请重新登录')
            else:
                cache.set(token_key, jwt_value, CACHE_TIMEOUT)
        except jwt.ExpiredSignature:
            raise AuthenticationFailed('Token失效，请重新登录')
        except ConnectionError:
            raise  AuthenticationFailed('redis服务器未启动！')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('非法用户')
        user = self.authenticate_credentials(payload)
        return user, jwt_value
