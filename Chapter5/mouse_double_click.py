from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

#这是在mac上执行的基于chrome浏览器上的测试，如下driver地址请根据实际情况进行修改。
chrome_driver_server = Service("/Users/jason118/Downloads/chromedriver")
driver  = webdriver.Chrome(service=chrome_driver_server)
driver.maximize_window()
driver.get('https://www.baidu.com')
driver.implicitly_wait(10)
driver.maximize_window()
try:
    element = driver.find_element(By.LINK_TEXT,u"新闻")
    ActionChains(driver).double_click(element).perform() #实现在新闻超链接上右键
    time.sleep(5)

except:
    print(u"元素定位有问题，请检查")
