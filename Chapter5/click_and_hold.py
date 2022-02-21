from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

#这是在mac上执行的基于chrome浏览器上的测试，如下driver地址请根据实际情况进行修改。
chrome_driver_server = Service("/Users/jason118/Downloads/chromedriver")
driver  = webdriver.Chrome(service=chrome_driver_server)
driver.maximize_window()
driver.get('https://www.sogou.com')
driver.implicitly_wait(10)
driver.maximize_window()
search_btn = driver.find_element(By.ID,"stb")

webdriver.ActionChains(driver).click_and_hold(search_btn).perform()
