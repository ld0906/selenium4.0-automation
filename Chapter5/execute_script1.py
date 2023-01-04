from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#这是在mac上执行的基于chrome浏览器上的测试，如下driver地址请根据实际情况进行修改。
chrome_driver_server = Service("/Users/jason118/Downloads/chromedriver")
driver  = webdriver.Chrome(service=chrome_driver_server)
driver.maximize_window()
driver.get("https://www.baidu.com")
js = "document.getElementById('kw').value = 'selenium'"
driver.execute_script(js)
#driver.quit()
