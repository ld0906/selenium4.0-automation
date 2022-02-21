from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


#这是在mac上执行的基于chrome浏览器上的测试，如下driver地址请根据实际情况进行修改。
chrome_driver_server = Service("/Users/jason118/Downloads/chromedriver")
driver  = webdriver.Chrome(service=chrome_driver_server)

driver.maximize_window()
driver.get("file:///Users/jason118/PycharmProjects/selenium4.0-automation/Chapter5/select.html")

select_element = driver.find_element(By.ID,"select_id")

#index索引是从0开始的，如下代码选择1，则是表示第二个选项。
Select(select_element).select_by_visible_text("option2")
#driver.quit()
