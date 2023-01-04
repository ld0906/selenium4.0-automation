# encoding = utf-8
import unittest
import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import math
chrome_driver_server = Service("./chromedriver")
# driver = webdriver.chrome()
class SuiteTest1(unittest.TestCase):  # 声明一个测试类
    def setUp(self):
        # 启动chrome浏览器
        self.driver = webdriver.Chrome(service=chrome_driver_server)

    def testBaidu(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.ID,"kw").clear()
        self.driver.find_element(By.ID,"kw").send_keys(u"python")
        self.driver.find_element(By.ID,"su").click()
        time.sleep(5)
        assert u"python" in self.driver.page_source, "页面中不存在要搜索的关键字！"

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(SuiteTest1("testBaidu"))
    file_name = "test1.html" #是为了设置生成的报表html文件地址。
    # fp = file(file_name,'wb')
    fp = open(file_name, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test_Report_Portal', description='Report_Description') #此步是为了设置报表页面的title和报表总结描述内容。
    runner.run(suite)
    fp.close()
    print("测试完成！")