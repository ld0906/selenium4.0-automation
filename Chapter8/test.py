from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time,os
import fateadm_api #引入斐斐打码验证码Python包，源文件在/Chapter8/fateadm_api.py


#这是在mac上执行的基于chrome浏览器上的测试，如下driver地址请根据实际情况进行修改。
chrome_driver_server = Service("/Users/jason118/Downloads/chromedriver")
driver  = webdriver.Chrome(service=chrome_driver_server)
driver.get("http://testdao.site/login")

time.sleep(20)

driver.find_element(By.XPATH,'//*[@id="side-menu"]/li[3]/a/span[1]').click()

time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="side-menu"]/li[3]/ul/li[5]/a').click()

time.sleep(10)