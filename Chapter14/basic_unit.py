#coding=utf-8
from base_unit import ParaCase
import time
from selenium.webdriver.common.by import By

class DetailCase(ParaCase):
	#以下函数是为了测试携程网登录功能。
    def test_login(self):
        time.sleep(2)
        self.driver.get('https://passport.ctrip.com/user/login?')
        self.driver.find_element(By.ID,'nloginname').send_keys("TimTest")
        self.driver.find_element(By.ID,'npwd').send_keys("TimTest")
        self.driver.find_element(By.ID,'nsubmit').click()
