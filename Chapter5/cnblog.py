from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#这是在mac上执行的基于chrome浏览器上的测试，如下driver地址请根据实际情况进行修改。
chrome_driver_server = Service("/Users/jason118/Downloads/chromedriver")
driver  = webdriver.Chrome(service=chrome_driver_server)
driver.maximize_window()
driver.get('https://www.cnblogs.com') #打开博客园主页面，首先在验证这个例子之前需要先注册好博客园账户。
print("before login:")
for cookie_detail in driver.get_cookies():
    print(cookie_detail)
time.sleep(30) #这里需要等待30秒，手动干预，进行博客园账号的输入。
print("after login:")
for cookie_detail in driver.get_cookies():
    print(cookie_detail)
driver.quit()
