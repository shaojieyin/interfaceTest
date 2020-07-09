# -*- coding: UTF-8 -*-
import unittest

class UserTestDemo(unittest.TestCase):
    def setUp(self):
        print("初始化类执行")
    def tearDown(self):
        print("类的回收执行")
        print("--------------------------")
    def testCase1(self):
        print("方法UserTestCase1 test case1")
    def testCase2(self):
        print("方法UserTestCase2 test case2")
    def testCase3(self):
        print("方法UserTestCase3 test case3")
    def testCase4(self):
        print("方法UserTestCase4 test case4")
if __name__ == '__main__':
    unittest.TestCase()