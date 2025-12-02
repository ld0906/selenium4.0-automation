#conding:uft-8
import  unittest
from Common.function import config_url
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#抽离单元测试中setUp与tearDown

class UnitBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = './chromedriver'
        chrome_driver_server = Service(path)
        cls.driver = webdriver.Chrome(service=chrome_driver_server)
        cls.driver.get(config_url())
        cls.driver.maximize_window()

    def tearDownClass(cls):
        cls.driver.quit()
