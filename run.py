# -*- coding: UTF-8 -*-
import unittest
import requests
import os # 加载路径使用

def load_all_case():
    #获取项目路径
    print(os.getcwd())
    # 拼接用例路径（这里是TestCase）路径
    case_path = os.path.join(os.getcwd(),"TestCase")
    print(case_path)
    #加载路径下所有Case
    discover = unittest.defaultTestLoader.discover(case_path,pattern='*Case.py',top_level_dir=None)
    print(discover)
    return discover
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(load_all_case())