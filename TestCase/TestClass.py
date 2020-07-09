import unittest

class TestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("类的初始化方法（）（）（）")
    @classmethod
    def tearDownClass(cls):
        print("类方法回收资源")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    def testCase1(self):
        print("UserTestCase2 test case1")

    def testCase2(self):
        print("UserTestCase2 test case2")
        self.assertEqual(1, 1)

    def testCase3(self):
        print("UserTestCase2 test case3")
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestClass("testCase3"))
    suite.addTest(TestClass("testCase2"))
    suite.addTest(TestClass("testCase1"))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)