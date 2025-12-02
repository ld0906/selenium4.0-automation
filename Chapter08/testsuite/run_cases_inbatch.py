import unittest
import os
#查询测试用例路径
case_path = os.path.join(os.getcwd())

def allcases():
    discover = unittest.defaultTestLoader.discover(case_path,pattern="case*.py",top_level_dir=None)
    print(discover)
    return discover

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(allcases())
