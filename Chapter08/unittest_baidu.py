from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest
import time
chrome_driver_server = Service("./chromedriver")
#driver  = webdriver.Chrome(service=chrome_driver_server)

class add(unittest.TestCase): #声明一个测试类
    def setUp(self):
        #启动chrome浏览器
        self.driver = webdriver.Chrome(service=chrome_driver_server)

    def testBaidu(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.ID,"kw").clear()
        self.driver.find_element(By.ID,"kw").send_keys(u"python")
        self.driver.find_element(By.ID,"su").click()
        time.sleep(5)
        assert u"python" in self.driver.page_source,"页面中不存在要搜索的关键字！"

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
