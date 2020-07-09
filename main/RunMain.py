# -*- coding: UTF-8 -*-
import unittest
import os
# 加载全部测试用
def load_all_test():
    # 用例路径
    case_path = os.path.join(os.getcwd(),"../TestCase")
    print(case_path)
    discover = unittest.defaultTestLoader.discover(case_path, pattern='*Case.py', top_level_dir=None)
    print(discover)
    return discover

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2).run(load_all_test())
