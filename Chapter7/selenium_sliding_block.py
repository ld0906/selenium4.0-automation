from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

#这是在mac上执行的基于chrome浏览器上的测试，如下driver地址请根据实际情况进行修改。
chrome_driver_server = Service("/Users/jason118/Downloads/chromedriver")
driver  = webdriver.Chrome(service=chrome_driver_server)
driver.maximize_window()
driver.get("file:///Users/jason118/PycharmProjects/selenium4.0-automation/Chapter7/selenium_sliding_block.html")
source_element = driver.find_element(By.ID,'sliding1')
target_element = driver.find_element(By.ID,'range1')
target_element_X_Offset = target_element.location.get("x")
target_element_Y_Offset = target_element.location.get("y")
# print(target_element_X_Offset)
# print(target_element_Y_Offset)
# print(source_element.location.get("x"))
# print(source_element.location.get("y"))
time.sleep(3)
ActionChains(driver).drag_and_drop_by_offset(source_element,700,0).perform()
#driver.quit()
