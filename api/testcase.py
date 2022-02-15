#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 后端设计数据库表内测试用例的增删改查

from flask import request
from flask_restful import Resource
import jenkins

from back_end.api.verify_token import auth

# 定义一个测试用例接口
from back_end.backend_server import db
from back_end.data_base.testcase_table import TestCase


class TestCaseAdd(Resource):
    method_decorators = [auth.login_required]

    def post(self):
        """
        新增用例
        1、把请求体中的数据发送到数据库
        例：r = requests.post('http://127.0.0.1:5000/testcase', json = {"nodeid":"123", "description":"a"})

        :return:
        """
        data = TestCase(**request.json)
        db.session.add(data)
        db.session.commit()
        return {'msg': 'ok'}


class TestCaseDelete(Resource):
    method_decorators = [auth.login_required]

    # get方法代表接收get请求
    def get(self):
        """
        删除测试用例
        例：http://127.0.0.1:5000/testcase?option=del_testcase&nodeid=123
        :return:
        """
        # 如果url中存在option参数为del_testcase代表要删除用例
        if 'nodeid' in request.args:
            # 利用nodeid参数指明要删除的用例
            nodeid = request.args.get('nodeid')
            # 查询用例后进行删除
            testcase = TestCase.query.filter_by(nodeid=nodeid).first()
            db.session.delete(testcase)
            db.session.commit()
            return {'msg': 'delete success!'}
        # 删除多个用例，比如：http://127.0.0.1:5000/testcase?option=del_testcases&nodeids=nodeid_1,nodeid_2
        elif 'nodeids' in request.args:
            # 利用nodeids参数指明要删除的用例
            nodeids = request.args.get('nodeids')
            for nodeid in nodeids.split(','):
                # 查询用例后进行删除
                testcase = TestCase.query.filter_by(nodeid=nodeid).first()
                db.session.delete(testcase)
            db.session.commit()
            return {'msg': 'delete success!'}


class TestCaseUpdate(Resource):
    method_decorators = [auth.login_required]

    def post(self):
        """
        更新测试用例
        例：r = requests.post('http://127.0.0.1:5000/testcase/update', json = {"nodeid":"nodeid_4", "description":"update"})
        :return:
        """
        request_body = request.json
        # 查询出要更新的数据
        testcase = TestCase.query.filter_by(nodeid=request_body.get('nodeid')).first()
        # 更新数据的描述信息
        testcase.description = request_body.get('description')
        db.session.commit()
        return {'msg': 'update success!'}


class TestCaseGet(Resource):
    method_decorators = [auth.login_required]

    def get(self):
        # 查找所有测试用例
        test_cases = TestCase.query.all()
        # 对测试用例进行格式化
        format_test_cases = [i.as_dict() for i in test_cases]
        return {'msg': 'OK', 'data': format_test_cases}


class TestCaseRun(Resource):
    method_decorators = [auth.login_required]

    def get(self):
        server = jenkins.Jenkins('http://localhost:8080', username='admin',
                                 password='11c5a90ad2c15dde4f2526bc23205e697e')
        server.build_job('iIniterface')
        return {'msg': 'OK', 'errcode': 200}

