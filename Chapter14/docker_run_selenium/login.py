import time,os
import fateadm_api

from functions import return_driver
from selenium.webdriver.common.by import By

def login(browser_type):
    driver = return_driver(browser_type)
    driver.get("http://124.223.13.201/login")
    filename = "capture.png"
    if os.path.exists(filename):
        os.remove(filename)

    ele1 = driver.find_element(By.XPATH, '//*[@id="signupForm"]/div[1]/div[2]/a/img')
    ele1.screenshot(filename)
    driver.find_element(By.NAME,'username').clear()
    driver.find_element(By.NAME,'username').send_keys("admin")
    driver.find_element(By.NAME,'password').clear()
    driver.find_element(By.NAME,'password').send_keys("admin123")


    #如下是调用斐斐打码代码，直接获取识别后的验证码值
    verification_code = str(fateadm_api.TestFunc())

    #在页面上输入验证码
    driver.find_element(By.NAME,'validateCode').send_keys(verification_code)

    #点击‘登录’按钮
    driver.find_element(By.ID,'btnSubmit').click()
    time.sleep(5)
