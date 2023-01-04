from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#这是在mac上执行的基于chrome浏览器上的测试，如下driver地址请根据实际情况进行修改。
chrome_driver_server = Service("/Users/jason118/Downloads/chromedriver")
driver  = webdriver.Chrome(service=chrome_driver_server)
driver.maximize_window()
driver.get("https://www.sogou.com")
#设置浏览器窗口大小，目的是让滚动条显示出来
driver.set_window_size(800,700)
#以下代码实现在搜索输入框中输入关键字"selenium"
jq = "$('#query').val('selenium')"
driver.execute_script(jq)
#以下代码实现点击"百度以下"按钮
jq = "$('#stb').click()"
driver.execute_script(jq)
#driver.quit()


