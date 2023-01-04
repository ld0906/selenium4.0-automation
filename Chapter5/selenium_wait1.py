from selenium import webdriver
from selenium.webdriver.support.color import Color
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.baidu.com")
driver.implicitly_wait(10) #表示设置的隐式等待时间为10秒，也即是最长的等待时间为10秒。
driver.find_element(By.NAME,'wd').send_keys("selenium")
