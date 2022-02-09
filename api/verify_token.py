#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import g
from flask_httpauth import HTTPBasicAuth

# 初始化auth
from data_base.user_table import User

auth = HTTPBasicAuth()

"""
auth的username在登录时，是用户名，在登录后，是token
"""


# 编写回调函数，当进行登录时，会回调此函数
@auth.verify_password
def verify_password(username, password):
    # 进行token校验
    user = User.check_token(username)
    # 如果校验结果错误，或超时，就认为此时是登录接口
    # 如果校验成功，就认为此时是其他接口
    if not user:
        # 从数据库中查用户信息
        user = User.query.filter_by(username=username).first()
        # 如果用户不存在或者密码不匹配，就校验失败
        if not user or user.password != password:
            return False

    # 如果token符合要求，或者用户名密码正确，执行下列操作
    # flask的g代表flask的本地线程变量 -> flask线程可共享使用
    g.user = user
    return True

