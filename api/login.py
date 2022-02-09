#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import g
from flask_restful import Resource
from api.verify_token import auth


class Login(Resource):
    # auth.login_required：是httpAuth的用法，添加了此装饰器的对象会回调校验方法
    # auth.login_required：代表给login接口添加一个装饰器，下面get表示，对get接口进行添加
    method_decorators = {'get': [auth.login_required]}

    def get(self):
        # 使用verify_password中，校验成功后的用户信息
        token = g.user.generate_token()
        return {"access_token": token}
