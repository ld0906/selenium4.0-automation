#coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def before_all(context):
    chrome_driver_server = Service("/Users/jason118/PycharmProjects/selenium4.0-automation/Chapter12/Chapter12.4/chromedriver")
    context.driver  = webdriver.Chrome(service=chrome_driver_server)

def after_tag(contex):
    time.sleep(5)
    context.driver.quit()
