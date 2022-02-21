from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


#这是在mac上执行的基于chrome浏览器上的测试，如下driver地址请根据实际情况进行修改。
chrome_driver_server = Service("/Users/jason118/Downloads/chromedriver")
driver  = webdriver.Chrome(service=chrome_driver_server)

#如下是打开本地文件，请根据实际地址进行改写
driver.get("file:///Users/jason118/PycharmProjects/selenium4.0-automation/Chapter4/relative_locator1.html")

#通过relative locator的below方式先获取到username input,然后再获取password input.
password_locator = locate_with(By.TAG_NAME,"input").below({By.ID: "id_username"})
password = driver.find_element(password_locator)
password.send_keys('password1')