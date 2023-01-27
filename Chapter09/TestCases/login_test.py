#_*_coding:utf-8_*_
import  time,unittest,HTMLTestRunner
from Chapter09.Common.function import project_path
from Chapter09.Common.excel_data import read_excel
from Chapter09.Common.function import config_url
from Chapter09.PageObject.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class login_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = read_excel(project_path() + "/Data/testdata.xlsx", 1)
        chrome_driver_server = Service("./chromedriver")
        cls.driver = webdriver.Chrome(service=chrome_driver_server)
        cls.driver.get(config_url())
        cls.driver.maximize_window()
    
    def test_01(self):
        login = LoginPage(self.driver)
        res = login.login_system(self.data.get(1)[0],self.data.get(1)[1])
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(login_test("test_01"))
    filepath = project_path() + "/Reports/report1.html"
    fp = open(filepath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='自动化测试报告', description="测试报告")
    runner.run(suiteTest)
    fp.close()