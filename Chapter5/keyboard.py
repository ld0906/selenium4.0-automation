from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#这是在mac上执行的基于chrome浏览器上的测试，如下driver地址请根据实际情况进行修改。
chrome_driver_server = Service("/Users/jason118/Downloads/chromedriver")
driver  = webdriver.Chrome(service=chrome_driver_server)
driver.maximize_window()
driver.get('https://www.baidu.com')
driver.implicitly_wait(10)
driver.maximize_window()
try:
  driver.find_element(By.ID,"kw").send_keys("Selenium*")
  time.sleep(3)
  driver.find_element(By.ID,"kw").send_keys(Keys.BACK_SPACE)
  #driver.find_element_by_id("kw").send_keys(Keys.ESCAPE)
  time.sleep(3)
except:
    print(u"元素定位有问题，请检查")
