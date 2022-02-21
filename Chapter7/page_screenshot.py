from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

#这是在mac上执行的基于chrome浏览器上的测试，如下driver地址请根据实际情况进行修改。
chrome_driver_server = Service("/Users/jason118/Downloads/chromedriver")
driver  = webdriver.Chrome(service=chrome_driver_server)
driver.maximize_window()
#driver.get("file:///Users/jason118/PycharmProjects/selenium4.0-automation/Chapter7/verification_code.html")
driver.get("https://id.qq.com/vc.html")
driver.maximize_window()
time.sleep(3)
driver.save_screenshot("verification_code.png")
