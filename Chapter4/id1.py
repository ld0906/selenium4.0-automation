from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#这是在mac上执行的基于chrome浏览器上的测试，如下driver地址请根据实际情况进行修改。
chrome_driver_server = Service("/Users/jason118/Downloads/chromedriver")
driver  = webdriver.Chrome(service=chrome_driver_server)
#打开百度首页
driver.get('https://www.baidu.com')
#在搜索输入框中输入文本"python"
driver.find_element(By.ID,'kw').send_keys('python')
