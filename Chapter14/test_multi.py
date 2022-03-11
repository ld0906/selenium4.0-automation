#coding=utf-8
import unittest
import  threading
from base_unit import ParaCase
from basic_unit import DetailCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_server = Service("./chromedriver")
# driver  = webdriver.Chrome(service=chrome_driver_server)
# driver.get("https://www.baidu.com")

firefox_driver_server = Service("./geckodriver")
# driver2 = webdriver.Firefox(service=firefox_driver_server)
# driver2.get("https://www.baidu.com")

#本例实现本地多个浏览器对同一脚本并发操作
#继承父类threading.Thread
class myThread (threading.Thread):   
    def __init__(self, device):
        threading.Thread.__init__(self)
        self.device=device

    def run(self):
        print ("Starting " + self.name)
        print ("Exiting " + self.name)
        run_suite(self.device)
#定义多线程实际要执行的操作
def run_suite(device):
    suite = unittest.TestSuite()
    suite.addTest(ParaCase.parametrize(DetailCase, param=device))
    unittest.TextTestRunner(verbosity=1).run(suite)

if __name__ == '__main__':
    #以下代是在本地通过同时访问多浏览器
    dr = [webdriver.Firefox(service=firefox_driver_server), webdriver.Chrome(service=chrome_driver_server)]
    for i in range(len(dr)):
        print(dr[i])
        th = myThread(dr[i])
        th.start()
        th.join()
