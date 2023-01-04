from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PIL import Image
import time

#这是在mac上执行的基于chrome浏览器上的测试，如下driver地址请根据实际情况进行修改。
chrome_driver_server = Service("/Users/jason118/Downloads/chromedriver")
driver  = webdriver.Chrome(service=chrome_driver_server)
driver.get("https://id.qq.com/vc.html")
time.sleep(2)
driver.save_screenshot("verification_code.png")
imgcode=driver.find_element(By.ID,"img")
imgcode.screenshot("t.jpg")
