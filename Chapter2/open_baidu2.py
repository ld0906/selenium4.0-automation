import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_server = Service("C:\\Users\\Administrator\\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_server)
driver.get('https://www.baidu.com')
driver.quit()