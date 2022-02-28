from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time,os

chrome_driver_server = Service("./chromedriver")

driver  = webdriver.Chrome(service=chrome_driver_server)
driver.get("http://testdao.site/index")