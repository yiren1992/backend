#!/usr/bin/env python
# -*- coding: utf-8 -*-
from back_end.backend_server import db


# 使用db可以让User类映射到数据库中的User表
class TestCase(db.Model):
    # db.Integer：是整型int，primary_key：代表主键，唯一标识一条数据，是一条数据的身份证
    id = db.Column(db.Integer, primary_key=True)
    nodeid = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=True)

    def as_dict(self):
        """
        返回测试用例的数据
        :return:
        """
        return {'id': self.id, 'nodeid': self.nodeid, 'description': self.description}


