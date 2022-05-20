from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.baidu.com")

#在百度首页，定义‘新闻’超链接元素的定义语句。
news_locator = (By.LINK_TEXT,'新闻')

#使用try 语句对元素的定义情况进行判断
try:
    WebDriverWait(driver,10,1).until(expected_conditions.presence_of_element_located(news_locator))
    print("元素成功定位到～")
except:
    print("元素没有定位到:(")
