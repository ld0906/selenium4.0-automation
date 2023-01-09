import time,os
import fateadm_api #引入斐斐打码验证码Python包，源文件在/Chapter8/fateadm_api.py

from functions import return_driver, id, name,xpath

def login():
    driver = return_driver()
    driver.get("http://124.223.13.201/login")
    filename = "capture.png"
    if os.path.exists(filename):
        os.remove(filename)

    ele1 = xpath('//*[@id="signupForm"]/div[1]/div[2]/a/img')
    ele1.screenshot(filename)
    name('username').clear()
    name('username').send_keys("admin")
    name('password').clear()
    name('password').send_keys("admin123")

    #如下是调用斐斐打码代码，直接获取识别后的验证码值
    verification_code = str(fateadm_api.TestFunc())

    #在页面上输入验证码
    name('validateCode').send_keys(verification_code)

    #点击‘登录’按钮
    id('btnSubmit').click()
    time.sleep(5)
