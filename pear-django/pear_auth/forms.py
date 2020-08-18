# -*- coding:utf-8 -*-
# @File  : pear-django/forms.py
# @Author: zlx
# @Date  : 2020-07-22 10:57
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
from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise forms.ValidationError('你的用户名太短了...')
        elif len(username) > 20:
            raise forms.ValidationError('你的用户名太长了...')
        else:
            result = User.objects.filter(username__exact=username)
            if len(result) > 0:
                raise forms.ValidationError('该用户名已被使用!')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len(password) < 6:
            raise forms.ValidationError('密码长度太短!')
        elif len(password) > 20:
            raise forms.ValidationError('密码长度太长!')
        return password


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')

        result = User.objects.filter(username__exact=username)
        if len(result) == 0:
            raise forms.ValidationError('该用户名不存在！')
        return username
