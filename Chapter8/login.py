from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time,os
import fateadm_api #引入斐斐打码验证码Python包，源文件在/Chapter8/fateadm_api.py


#这是在mac上执行的基于chrome浏览器上的测试，如下driver地址请根据实际情况进行修改。
chrome_driver_server = Service("/Users/jason118/Downloads/chromedriver")
driver  = webdriver.Chrome(service=chrome_driver_server)
driver.get("http://localhost/login")
filename = "capture.png"
if os.path.exists(filename):
    os.remove(filename)

ele1 = driver.find_element(By.XPATH,'//*[@id="signupForm"]/div[1]/div[2]/a/img')
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

time.sleep(20)