from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_server = Service("./chromedriver")
driver  = webdriver.Chrome(service=chrome_driver_server)

'''
函数 return_driver是为了返回driver对象
'''
def return_driver():
    return driver

'''
函数 name是为了用NAME方式来定位元素
'''
def name(locator):
    return driver.find_element(By.NAME,locator)

'''
函数 id是为了用ID方式来定位元素
'''
def id(locator):
    return driver.find_element(By.ID,locator)

'''
函数 xpath是为了用XPATH方式来定位元素
'''
def xpath(locator):
    return driver.find_element(By.XPATH,locator)