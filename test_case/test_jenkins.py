#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jenkins


def test_jenkins():
    # password='11c5a90ad2c15dde4f2526bc23205e697e'，可用Jenkins喷值得用户token代替密码
    server = jenkins.Jenkins('http://localhost:8080', username='admin', password='11c5a90ad2c15dde4f2526bc23205e697e')
    # 打印job的数量
    print(server.jobs_count())
    print(server.build_job('iIniterface'))

