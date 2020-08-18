# -*- coding:utf-8 -*-
# @File  : pear-django/utils.py
# @Author: zlx
# @Date  : 2020-07-22 9:41
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
import random
from hashlib import md5
from common_constant import TOKEN_EXPIRE_TIME, PREFIX_USER_TOKEN

'''
随机生成用户加密盐值
'''


def randomGen(place=8):
    base = "qwertyuioplkjhgfdsazxcvbnmQAZWSXEDCRFVTGBYHNUJMIKLOP0123456789"
    salt = ""
    for i in range(place):
        salt += base[random.randint(0, len(base) - 1)]
    return salt


def encrypt(password, salt):
    md5_obj = md5()
    md5_obj.update(password + salt)
    return md5_obj.hexdigest()


