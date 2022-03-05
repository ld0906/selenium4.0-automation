from login import login
from add_position import add_position
from functions import read_excel
from functions import log
import HTMLTestRunner
import unittest
import time


class system_add_position(unittest.TestCase):

    def test_add_position(self):
        log("Read Excel Files to get test data.")
        dict1 = read_excel("position_data.xlsx",0)
        log("Begin to log in system.")
        login()
        time.sleep(2)
        log("Log in system done.")
        log("Begin to add position in system.")
        #测试添加岗位信息场景
        add_position(dict1[0][0],dict1[0][1])
        log("Add position done.")
        time.sleep(2)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(system_add_position("test_add_position"))
    file_name = "report_add_position.html"
    fp = open(file_name,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test_Report_Portal', description='Report_Description') #此步是为了设置报表页面的title和报表总结描述内容。
    runner.run(suite)
    fp.close()