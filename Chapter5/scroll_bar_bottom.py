from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#这是在mac上执行的基于chrome浏览器上的测试，如下driver地址请根据实际情况进行修改。
chrome_driver_server = Service("/Users/jason118/Downloads/chromedriver")
driver  = webdriver.Chrome(service=chrome_driver_server)
driver.maximize_window()
driver.get("https://www.sogou.com")
#设置浏览器窗口大小，目的是让滚动条显示出来
driver.set_window_size(800,700)
driver.find_element(By.ID,'query').send_keys("Python")
time.sleep(2)
driver.find_element(By.ID,'stb').click()
time.sleep(2)
#滚动条滑动到底部
js = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)
#driver.quit()

