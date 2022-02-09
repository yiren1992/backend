#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 配置数据库的详细信息
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test1_user:test1_user@localhost:3306/test1'
# 初始化一个db
db = SQLAlchemy(app)
# 将flask实例加载到flask-restful中
app.config["SECRETY_KEY"] = "SDET17"
api = Api(app)
# 使用 CORS 解决前后端 同源问题
CORS(app)


def router():
    from api.testcase import TestCaseAdd
    api.add_resource(TestCaseAdd, '/testcase/add')
    from api.testcase import TestCaseDelete
    api.add_resource(TestCaseDelete, '/testcase/delete')
    from api.testcase import TestCaseUpdate
    api.add_resource(TestCaseUpdate, '/testcase/update')
    from api.testcase import TestCaseGet
    api.add_resource(TestCaseGet, '/testcase/get')
    from api.login import Login
    api.add_resource(Login, '/login')


if __name__ == '__main__':
    # 删库，如果存在重要数据，一定要先手动备份数据，再执行该操作
    # db.drop_all()
    # # db.create_all()
    # for i in range(1, 20):
    #     data = TestCase(nodeid=f'nodeid_{i}')
    #     db.session.add(data)
    # db.session.commit()
    router()
    app.run(debug=True)
