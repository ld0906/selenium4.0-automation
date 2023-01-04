from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#导入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains


#这是在mac上执行的基于chrome浏览器上的测试，如下driver地址请根据实际情况进行修改。
chrome_driver_server = Service("/Users/jason118/Downloads/chromedriver")
driver  = webdriver.Chrome(service=chrome_driver_server)

driver.maximize_window()
driver.get("https://www.baidu.com")
bg_config = driver.find_element(By.ID,'s-usersetting-top')

#这里使用方法move_to_element模拟将鼠标放置在超链接"设置"上方，即是模拟鼠标悬停。
ActionChains(driver).move_to_element(bg_config).perform()

#鼠标悬停时，定位元素，超链接"搜索设置"；然后实现单击操作。
driver.find_element(By.LINK_TEXT,"搜索设置").click()

driver.quit()
