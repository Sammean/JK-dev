#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：Jk-dev -> 01Test
@IDE    ：PyCharm
@Author ：Sammean Shaw
@Date   ：2024/11/15 11:45
@Desc   ：
==================================================
"""
import os
import pytest  # 导入pytest模块
import allure

@allure.feature('Test')
def test_func():  # 测试用例
    print('test_func')

@allure.feature('ModelDeploy')
class TestUnit():  # 测试套件
    def test_a(self):  # 测试用例，第一个测试方法
        print('test_a')

    def test_b(self):  # 测试用例，第二个测试方法
        print('test_b')


if __name__ == "__main__":
    pytest.main(["-s", "01_test.py",
                 "--alluredir", "reports", "--clean-alluredir"])
    # os.system("allure server ./reports")