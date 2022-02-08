#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests


class TestLogin:
    BASE_URL = "http://127.0.0.1:5000"

    def setup(self):
        pass

    def test_login(self):
        # auth 表示要输入的校验信息，比如账号和密码
        r = requests.get(self.BASE_URL + '/login', auth=('test1', '123456'))
        assert "access_token" in r.json()

        r = requests.get(self.BASE_URL + '/login', auth=('test1', '16'))
        assert r.status_code == 401
