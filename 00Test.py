#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：ESU-dev -> 00Test
@IDE    ：PyCharm
@Author ：Sammean Shaw
@Date   ：2024/11/15 11:08
@Desc   ：
==================================================
"""
import unittest
import allure

@allure.feature('ModelDeploy')
class ModelDeployUnitTest(unittest.TestCase):
    def setUp(self) -> None:  # 调用setUp
        super().setUp()
        print('Before Test')
    def test_IQE_01(self):
        print('Test 1...')

    def test_onnxrunnig_02(self):
        print('Test 2!!!')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ModelDeployUnitTest("test_IQE_01"))
    runner = unittest.TextTestRunner()
    runner.run(suite)