#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests


class TestTestCase:
    def test_get_right_testcase(self):
        r = requests.get("http://127.0.0.1:5000/login", auth=('test1', '123456'))
        token = r.json().get('access_token')
        r = requests.get('http://127.0.0.1:5000/testcase/get', auth=(token, ''))
        assert r.status_code == 200
        assert r.json().get('msg') == 'OK'

    def test_get_error_testcase(self):
        token = ''
        r = requests.get('http://127.0.0.1:5000/testcase/get', auth=(token, ''))
        assert r.status_code == 401
