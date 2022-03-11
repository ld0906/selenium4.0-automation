#coding=utf-8
from thred_unit.basic_unit import ParaCase
import time

class DetailCase(ParaCase):
	#以下函数是为了测试携程网登录功能。
    def test_login(self):
        time.sleep(2)
        self.driver.get('https://passport.ctrip.com/user/login?')
        self.driver.find_element_by_id('nloginname').send_keys("TimTest")
        self.driver.find_element_by_id('npwd').send_keys("TimTest")
        self.driver.find_element_by_id('nsubmit').click()
