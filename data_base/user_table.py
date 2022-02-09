#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# 用于生成具有时间维护的token
from itsdangerous import TimedJSONWebSignatureSerializer, BadSignature, SignatureExpired

# 配置token种子
from backend_server import app, db


class User(db.Model):
    """
    用户表，需要有账号，密码，邮箱
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # 创建日期

    # 打印类User的信息
    def __repr__(self):
        return f'<User {self.username}>'

    def generate_token(self, expires_in=3 * 3600):
        """
        生成token
        """
        # app.config["SECRETY_KEY"]：token种子，用于生成token，其值可以是随机的
        # expires_in代表超时时间
        serializer = TimedJSONWebSignatureSerializer(app.config["SECRETY_KEY"], expires_in=expires_in)
        token_id = self.username + self.password + str(datetime.now())
        # dumps用于反序列化（把python对象转化成字符串），生成token
        token = serializer.dumps({"id": self.id, "token_id": token_id}).decode()
        return token

    # 类方法，方便外界进行调用，同时此方法不会用到对象中的数据
    @classmethod
    def check_token(cls, token):
        """
        校验token
        :return: User or None
        """
        serializer = TimedJSONWebSignatureSerializer(app.config["SECRETY_KEY"])
        try:
            # loads用于序列化，把token转换成对象
            token_loads_result = serializer.loads(token)
        # 如果token校验失败，会抛出BadSignature
        # SignatureExpired：token超时异常
        except(BadSignature, SignatureExpired):
            return None
        # User.query.get:利用id找到User表中的一个字段
        return User.query.get(token_loads_result["id"])


#
# class Task(db.Model):
#     task_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=False, nullable=True)
#
#     def __repr__(self):
#         return '<User %r>' % self.name


if __name__ == '__main__':
    # 删库，如果存在重要数据，一定要先手动备份数据，再执行该操作
    db.drop_all()
    # 在远程数据库中创建表
    db.create_all()
