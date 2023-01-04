from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PIL import Image
import time

#这是在mac上执行的基于chrome浏览器上的测试，如下driver地址请根据实际情况进行修改。
chrome_driver_server = Service("/Users/jason118/Downloads/chromedriver")
driver  = webdriver.Chrome(service=chrome_driver_server)
#以下步骤是直接打开车次预订的页面
driver.get("file:///Users/jason118/PycharmProjects/selenium4.0-automation/Chapter7/fuzzy_search.html")
driver.find_element(By.XPATH,"//*[contains(@id,'div-body2')]/button[1]").click()
driver.find_element(By.XPATH,"//*[contains(@id,'div-body2')]/button[2]").click()
