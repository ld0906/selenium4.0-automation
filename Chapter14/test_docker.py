#coding=utf-8
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from base_unit import ParaCase
from basic_unit import DetailCase
import  threading,unittest

#本例通过selenium server并发操作
#继承父类threading.Thread
class myThread (threading.Thread):   
    def __init__(self, device):
        threading.Thread.__init__(self)
        self.device=device

    def run(self):
        print ("Starting " + self.name)
        print ("Exiting " + self.name)
        run_suite(self.device)

def run_suite(device):
    suite = unittest.TestSuite()
    suite.addTest(ParaCase.parametrize(DetailCase, param=device))
    unittest.TextTestRunner(verbosity=1).run(suite)
if __name__ == '__main__':
    url='http://127.0.0.1:4444/wd/hub'
    chrome_capabilities = {
        "browserName": "chrome",
        "version": "",
        "platform": "ANY",
        "javascriptEnabled": True,
        # "marionette": True,
    }
    browser = [DesiredCapabilities.CHROME,DesiredCapabilities.FIREFOX]
    driver1 =  webdriver.Remote(command_executor=url,desired_capabilities=chrome_capabilities)
    driver2 =  webdriver.Remote(command_executor=url,desired_capabilities=DesiredCapabilities.FIREFOX)
    th1 =  myThread(driver1)
    th1.start()
    th1.join()
    th2 =  myThread(driver2)
    th2.start()
    th2.join()

