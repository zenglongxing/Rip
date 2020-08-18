from django.shortcuts import render, HttpResponse
from .forms import *
from django.contrib import auth
from rest_framework.views import APIView
from rest_framework_jwt.serializers import jwt_payload_handler
from rest_framework_jwt.serializers import jwt_encode_handler
from webui.utils.Result import ok, error, loginSuccess
from django.core.cache import cache
from crawl.crawl_method import login, get_desc, get_photo_method, get_movie_by_actor
from pear.settings import CACHE_TIMEOUT, CACHE_PREFIX
import json


# Create your views here.

def register(request):
    if request.method == 'POST':
        params = json.loads(request.body)
        username = params['username']
        password = params['password']
        user = User.objects.create_user(username=username, password=password)
    return ok({})


class LoginAPIView(APIView):
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        params = json.loads(request.body)
        username = params['username']
        password = params['password']
        user_obj = auth.authenticate(username=username, password=password)
        if user_obj and user_obj.is_active:
            payload = jwt_payload_handler(user_obj)
            token = jwt_encode_handler(payload)
            token_key = CACHE_PREFIX + token
            user_info = {
                'username': username,
            }
            cache.set(token_key, token, CACHE_TIMEOUT)
            login()  # 爬虫登陆网站
            return loginSuccess(user_info=user_info, token=token)
        else:
            return error('用户名或密码错误!')
