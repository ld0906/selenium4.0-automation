from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#这是在mac上执行的基于chrome浏览器上的测试，如下driver地址请根据实际情况进行修改。
chrome_driver_server = Service("/Users/jason118/Downloads/chromedriver")
driver  = webdriver.Chrome(service=chrome_driver_server)

driver.get('https://trains.ctrip.com/')
driver.maximize_window()
driver.execute_script("window.scrollTo(0,1000)")