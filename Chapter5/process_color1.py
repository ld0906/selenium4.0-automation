from selenium import webdriver
from selenium.webdriver.support.color import Color
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.baidu.com")
#获取‘百度一下'的背景色 #4e6ef2
baidu_background_color = Color.from_string(driver.find_element(By.ID,'su').value_of_css_property('background-color'))
print(baidu_background_color.hex)
